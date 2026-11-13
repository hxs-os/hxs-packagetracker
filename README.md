# packagetracker

this is the HxS packagetracker, a collection of `ebs(5)` formulae inspired in [`freebsd-ports`](https://github.com/freebsd/freebsd-ports) and [`void-packages`](https://github.com/void-linux/void-packages).

each formulae can be built using the `ebs(1)` build system, found in the `xpt` / `xpt.static` package.

## formulae

### first-party formulae

these formulae build packages from first-class HxS projects.

| package    | static counterpart | description                                          |
| ---------- | ------------------ | ---------------------------------------------------- |
| `xpt`      | `xpt.static`       | the xpt package manager                              |
| `shush`    | `shush.static`     | the shush shell                                      |
| `hbase`    | `hbase.static`     | the hbase utility collection                         |
| `adam`     | `adam.static`      | the adam init system                                 |
| `hello`    | —                  | a hello world program, doubles as an example formula |
| `pxbase`   | `pxbase.static`    | (f.k.a hbase) the pxbase utility collection          |
| `sharbase` | `sharbase.static`  | a suite of `shar(1)`-related utilities               |
| `rswc`     | `rswc.static`      | a tiny utility to download files from the network    |
| `hxs-base` | —                  | base files for an HxS system                         |

### third-party formulae

these formulae build packages from third-party projects, regardless of their origin.

| package             | static counterpart | description                                                     |
| ------------------- | ------------------ | --------------------------------------------------------------- |
| `musl`              | —                  | implementation of the C standard library                        |
| `zlib`              | —                  | a lossless data-compression library                             |
| `zstd`              | —                  | fast real-time compression algorithm                            |
| `pkgconf`           | —                  | package compiler and linker metadata toolkit                    |
| `openssl`           | —                  | robust, commercial-grade, full-featured, TLS toolkit            |
| `ncurses`           | —                  | software emulation of curses                                    |
| `sqlite3`           | —                  | a small, fast, self-contained SQL database engine               |
| `bzip2`             | —                  | block-sorting file compression format                           |
| `xz`                | —                  | C89 implementation of the .xz file format                       |
| `libedit`           | —                  | autotool- and libtoolized port of the NetBSD editline library   |
| `libarchive`        | —                  | multi-format archive and compression library                    |
| `dash`              | `dash.static`      | debian almquist shell                                           |
| `man-pages`         | —                  | manual pages for GNU+Linux                                      |
| `fakeroot`          | —                  | gives a fake root environment for package building              |
| `util-linux`        | —                  | low-level system utilities for a Linux system                   |
| `shadow`            | —                  | utilities for user and group administration                     |
| `linux-headers`     | —                  | headers for linux kernel interfaces                             |
| `openvi`            | —                  | portable implementation of vi, derived from openbsd             |
| `diffutils`         | —                  | utilities to compare files                                      |
| `make`              | —                  | GNU make                                                        |
| `grep`              | —                  | searches one or more files for patterns                         |
| `sed`               | —                  | non-interactive command line editor                             |
| `findutils`         | —                  | basic directory searching utilities                             |
| `gawk`              | —                  | GNU implementation of the awk programming language              |
| `gzip`              | —                  | GNU data compression utility                                    |
| `patch`             | —                  | applies textual changes to files                                |
| `curl`              | —                  | URL transfer utility and library                                |
| `file`              | —                  | file type identification utility                                |
| `ca-certificates`   | —                  | Mozilla CA certificate bundle                                   |
| `binutils`          | —                  | GNU collection of binary tools                                  |
| `m4`                | —                  | GNU m4 macro processor                                          |
| `bison`             | —                  | general-purpose parser generator                                |
| `flex`              | —                  | the fast lexical analyzer                                       |
| `gmp`               | —                  | gnu multiple precision arithmetic library                       |
| `mpc`               | —                  | multiple precision complex arithmetic library                   |
| `mpfr`              | —                  | multiple-precision floating-point computations library          |
| `libisl`            | —                  | integer set library                                             |
| `gcc`               | —                  | GNU compiler collection                                         |
| `autoconf`          | —                  | m4 macros to generate configure scripts                         |
| `automake`          | —                  | m4 macros to generate Makefile.in files                         |
| `libtool`           | —                  | generic library support script                                  |
| `perl`              | —                  | Perl programming language                                       |
| `gettext`           | —                  | utilities for internalization and localization                  |
| `texinfo`           | —                  | the GNU documentation format                                    |
| `python`            | —                  | Python programming language                                     |
| `iana-etc`          | —                  | `/etc/protocols` and `/etc/services` provided by IANA           |
| `dhcpcd`            | —                  | dhcp / ipv4ll / ipv6ra / dhcpv6 client                          |
| `kmod`              | —                  | utilities to load Linux kernel modules                          |
| `procps-ng`         | —                  | utilities to monitor system resources                           |
| `python-flit-core`  | —                  | a minimal PEP 517 build backend                                 |
| `python-packaging`  | —                  | core utilities for Python package metadata and version handling |
| `python-setuptools` | —                  | built-package format for Python distributions                   |
| `python-wheel`      | —                  | Python package build system and distribution utilities          |
| `meson`             | —                  | the meson build system                                          |
| `git`               | —                  | distributed version control system                              |
| `samurai`           | —                  | ninja-compatible build tool written in C99                      |
| `mandoc`            | —                  | a suite of tools for manual pages                               |
| `toybox`            | `toybox.static`    | common Linux command-line utilities bundled in a single binary  |
| `less`              | —                  | free and open-source file pager                                 |
| `sinit`             | `sinit`            | suckless init                                                   |
| `sbase`             | `sbase.static`     | collection of unix tools                                        |
| `ubase`             | `ubase.static`     | collection of unportable tools, similar in spirit to util-linux |
