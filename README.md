# HxS PackageTracker

the HxS PackageTracker is a collection of `ebs(5)` formulae used to build packages for HxS.

the HxS PackageTracker is heavily inspired by FreeBSD Ports and [`void-packages`](https://github.com/void-linux/void-packages).

## formulae

further information about each formula is found in the formula metadata and [`releases.json`](releases.json).

### first-party formulae

these are formulae for first-party packages, i.e. packages written for HxS.

| package | static counterpart | description                                          |
| ------- | ------------------ | ---------------------------------------------------- |
| `xpt`   | `xpt.static`       | the xpt package manager                              |
| `shush` | `shush.static`     | the shush shell                                      |
| `hbase` | `hbase.static`     | the hbase utility collection                         |
| `adam`  | `adam.static`      | the adam init system                                 |
| `hello` | —                  | a hello world program, doubles as an example formula |

### third-party formulae

these are formulae for third-party packages, i.e. packages not written for HxS.

| package           | static counterpart | description                                                   |
| ----------------- | ------------------ | ------------------------------------------------------------- |
| `musl`            | —                  | implementation of the C standard library                      |
| `zlib`            | —                  | a lossless data-compression library                           |
| `zstd`            | —                  | fast real-time compression algorithm                          |
| `pkgconf`         | —                  | package compiler and linker metadata toolkit                  |
| `openssl`         | —                  | robust, commercial-grade, full-featured, TLS toolkit          |
| `ncurses`         | —                  | software emulation of curses                                  |
| `sqlite3`         | —                  | a small, fast, self-contained SQL database engine             |
| `bzip2`           | —                  | block-sorting file compression format                         |
| `xz`              | —                  | C89 implementation of the .xz file format                     |
| `libedit`         | —                  | autotool- and libtoolized port of the NetBSD editline library |
| `libarchive`      | —                  | multi-format archive and compression library                  |
| `dash`            | `dash.static`      | debian almquist shell                                         |
| `man-pages`       | —                  | manual pages for GNU+Linux                                    |
| `fakeroot`        | —                  | gives a fake root environment for package building            |
| `util-linux`      | —                  | low-level system utilities for a Linux system                 |
| `shadow`          | —                  | utilities for user and group administration                   |
| `linux-headers`   | —                  | headers for linux kernel interfaces                           |
| `openvi`          | —                  | portable implementation of vi, derived from openbsd           |
| `diffutils`       | —                  | utilities to compare files                                    |
| `make`            | —                  | GNU make                                                      |
| `grep`            | —                  | searches one or more files for patterns                       |
| `sed`             | —                  | non-interactive command line editor                           |
| `findutils`       | —                  | basic directory searching utilities                           |
| `gawk`            | —                  | GNU implementation of the awk programming language            |
| `gzip`            | —                  | GNU data compression utility                                  |
| `patch`           | —                  | applies textual changes to files                              |
| `curl`            | —                  | URL transfer utility and library                              |
| `file`            | —                  | file type identification utility                              |
| `ca-certificates` | —                  | Mozilla CA certificate bundle utility                         |
| `binutils`        | —                  | GNU collection of binary tools                                |
| `m4`              | —                  | GNU m4 macro processor                                        |

### how to build

each formula can be built with:

```sh
ebs build package/package-version.ebs
```

> the `ebs(1)` build system can be found as a shell script in the `xpt` package, as part of the `ebt` subsystem.
