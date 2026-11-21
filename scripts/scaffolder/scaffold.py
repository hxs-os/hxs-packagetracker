#!/usr/bin/env python3
import sys
from pathlib import Path
from string import Template

BASE_FORMULA = """#!/bin/sh

#shellcheck disable=SC2034
#shellcheck disable=SC2154
#shellcheck disable=SC2086

#ebs.formulae
ebsver=1

pkgname=$NAME
pkgver=$VERSION
pkgsrc=
pkgchecksum=sha256:
pkgdesc=""
pkgmaintainer=""
pkglicense=""
pkghomepage=""
pkgcheck=true
pkgdeps="musl"
# pkgtriggers="man"
# pkgprovides="lib$NAME"

build() {
    ./configure ${CONFIGUREFLAGS:-} --prefix=/usr
    make
}

check() {
    make check
}

package() {
    "${1:-fakeroot}" make install DESTDIR="$pkgdir"
}

"""

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"usage: {sys.argv[0]!s} name version", file=sys.stderr)
        sys.exit(1)

    name = sys.argv[1]
    version = sys.argv[2]

    path = Path(f"{name!s}/{name!s}-{version!s}.ebs")
    if path.exists():
        print(f"! '{path!s}' already exists", file=sys.stderr)
        sys.exit(1)

    (path.parent / "files").mkdir(parents=True, exist_ok=True)

    print(f"> creating {name!s}/{name!s}-{version!s}.ebs")

    formula = Template(BASE_FORMULA).safe_substitute({"NAME": name, "VERSION": version})

    path.write_text(formula)

    print("> done")
