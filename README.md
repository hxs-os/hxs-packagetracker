# HxS PackageTracker

the HxS PackageTracker is a collection of `ebs(5)` formulae used to build packages for HxS.

the HxS PackageTracker is heavily inspired by FreeBSD Ports and [`void-packages`](https://github.com/void-linux/void-packages).

## formulae

further information about each formula is found in the formula metadata and `releases.json`.

### first-party formulae

these are formulae for first-party packages, i.e. packages written for HxS.

| package | static counterpart | description                  |
| ------- | ------------------ | ---------------------------- |
| `xpt`   | `xpt.static`       | the xpt package manager      |
| `shush` | `shush.static`     | the shush shell              |
| `hbase` | `hbase.static`     | the hbase utility collection |

### third-party formulae

these are formulae for third-party packages, i.e. packages not written for HxS.

| package   | static counterpart | description                                          |
| --------- | ------------------ | ---------------------------------------------------- |
| `musl`    | —                  | implementation of the C standard library             |
| `zlib`    | —                  | a lossless data-compression library                  |
| `zstd`    | —                  | fast real-time compression algorithm                 |
| `pkgconf` | —                  | package compiler and linker metadata toolkit         |
| `openssl` | —                  | robust, commercial-grade, full-featured, TLS toolkit |
| `ncurses` | —                  | software emulation of curses                         |
| `sqlite3` | —                  | a small, fast, self-contained SQL database engine    |
| `bzip2`   | —                  | block-sorting file compression format                |

### how to build

each formula can be built with:

```sh
ebs build package/package-version.ebs
```

> the `ebs(1)` build system can be found as a shell script in the `xpt` package, as part of the `ebt` subsystem.
