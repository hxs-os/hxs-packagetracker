#!/usr/bin/env python3

import json
from pathlib import Path

root = Path(__file__).resolve().parent
database = root / "releases.json"

packages = {}

for path in sorted(root.rglob("*.ebs")):
    if not path.is_file():
        raise FileNotFoundError(f"{path!s} is not a file")

    relative = path.relative_to(root)
    name, formula = relative.parts

    static = name.endswith(".static")
    if static:
        name = name.removesuffix(".static")

    if not name:
        raise ValueError("name cannot be empty")

    _, version = formula.removesuffix(".ebs").rsplit("-", maxsplit=1)

    entry = packages.setdefault(
        name,
        {
            "name": name,
            "versions": {},
        },
    )

    version_entry = entry["versions"].setdefault(
        version,
        {
            "static": {"has_static": False},
        },
    )

    version_entry["path"] = str(relative)

    if static:
        version_entry["static"]["has_static"] = True
        version_entry["static"]["path"] = str(relative)

table = {"packagetracker": 1, "packages": []}
table["packages"] = sorted(packages.values(), key=lambda entry: entry["name"])

with database.open("w", encoding="utf-8") as file:
    json.dump(table, file, indent=2)
    file.write("\n")
