#!/usr/bin/env python3
import json
import re
from pathlib import Path
from string import Template

from license_expression import ExpressionError, get_spdx_licensing

spdx = get_spdx_licensing()

# packages to filter
PACKAGE_FILTERS = {"hbase"}


def vkey(v: str) -> list:
    return [int(n) for n in re.findall(r"\d+", v)]


def parse_license(v: str) -> dict:
    v = v.strip()

    if not v:
        raise ValueError("empty license expression")

    try:
        parsed = spdx.parse(v, strict=True)
    except ExpressionError as exc:
        raise ValueError(f"invalid spdx license expression: {v!s}: {exc}")

    return {"expression": str(parsed), "identifiers": spdx.license_keys(parsed)}


def maintainer_email(value: str) -> str:
    match = re.search(r"<([^<>]+)>", value)
    return match.group(1).strip() if match else value.strip()


def parse_formula(p: Path) -> dict:
    d = {}

    cont = p.read_text()

    for lin in cont.splitlines():
        if lin.startswith(("build()", "prepare()")):
            break

        if not lin or lin.startswith("#"):
            continue

        if "=" not in lin:
            continue

        k, v = lin.split("=", 1)
        d[k] = Template(v.strip("'\" ")).safe_substitute(d)

    return d


def format_entry(d: dict) -> dict:
    name = d["pkgname"]

    if name.endswith(".static") or name in PACKAGE_FILTERS:
        return {}

    emails = [maintainer_email(em) for em in d["pkgmaintainer"].split(",")]
    license = parse_license(d["pkglicense"])

    return {
        "name": name,
        "version": d["pkgver"],
        "homepage": d["pkghomepage"],
        "recipe": f"https://github.com/hxs-os/hxs-packagetracker/blob/main/{d['pkgname']!s}/{d['pkgname']!s}-{d['pkgver']!s}.ebs",
        "source": d["pkgsrc"],
        "summary": d["pkgdesc"],
        "license": license["expression"],
        "license_ids": license["identifiers"],
        "maintainers": emails,
    }


def create_tree(tracker_root: Path) -> list:
    best = {}

    for formula in sorted(tracker_root.rglob("*.ebs")):
        ent = format_entry(parse_formula(formula))
        if not ent:
            continue

        cur = best.get(ent["name"])
        if cur is None or vkey(ent["version"]) > vkey(cur["version"]):
            best[ent["name"]] = ent

    return sorted(best.values(), key=lambda e: e["name"])


if __name__ == "__main__":
    root = Path(".")
    version_file = root / "versions.json"

    with version_file.open("w", encoding="utf-8") as fp:
        json.dump(create_tree(root), fp, indent=2)
        fp.write("\n")
