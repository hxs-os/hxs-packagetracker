# The HxS PackageTracker

[![Update versions.json](https://github.com/hxs-os/hxs-packagetracker/actions/workflows/update-versions.yml/badge.svg)](https://github.com/hxs-os/hxs-packagetracker/actions/workflows/update-versions.yml)
[![Lint Formulae](https://github.com/hxs-os/hxs-packagetracker/actions/workflows/lint-formulae.yml/badge.svg)](https://github.com/hxs-os/hxs-packagetracker/actions/workflows/lint-formulae.yml)

This is the HxS PackageTracker, a collection of `ebs(5)` formulae inspired by [`freebsd-ports`](https://github.com/freebsd/freebsd-ports) and [`void-packages`](https://github.com/void-linux/void-packages).

> Further information about using PackageTracker can be found in [The HxS Handbook](https://handbook.hxs.juanvel400.com/packagetracker).

## Building Formula

Use `ebs(1)` from the `xpt` package:

```sh
ebs build <name>/<name>-<version>.ebs
```

Packages are built as `.xpt` files, installable using `xpt(8)`:

```sh
xpt -if <name>-<version>.xpt
```

## Writing Formulae

See `ebs(5)` for the full formula format.

To scaffold a formula, use:

```sh
python3 scripts/scaffolder/scaffold.py <name> <version>
```

## Submitting Formulae

View [CONTRIBUTING.md](CONTRIBUTING.md) for instructions on submitting formulae.

## Index

The [`versions.json`](versions.json) file contains an automatically-generated index of all formula in PackageTracker.

## License

Formulae and Scripts are licensed under [BSD-3-Clause](https://spdx.org/licenses/BSD-3-Clause.html), see [LICENSE](LICENSE).

Patches are subject to the licensing terms of their respective projects, or BSD-3-Clause as a default.
