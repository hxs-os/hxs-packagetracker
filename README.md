# HxS PackageTracker

the HxS PackageTracker is a collection of `ebs(5)` formulae used to build the packages that make up a complete HxS system.

## formulae

further information about each formula is found in the formula metadata.

### first-party formulae

these are formulae for first-party packages, i.e. packages written for HxS.

| package | static counterpart | description                  |
| ------- | ------------------ | ---------------------------- |
| `xpt`   | `xpt.static`       | the xpt package manager      |
| `shush` | `shush.static`     | the shush shell              |
| `hbase` | `hbase.static`     | the hbase utility collection |

### third-party formulae

these are formulae for third-party packages, i.e. packages not written for HxS.

| package | static counterpart | description                              |
| ------- | ------------------ | ---------------------------------------- |
| `musl`  | —                  | implementation of the C standard library |
| `zlib`  | —                  | a lossless data-compression library      |

### how to build

each formula can be built with:

```sh
ebs build package/package-version.ebs
```

> the `ebs(1)` build system can be found as a shell script in the `xpt` package, as part of the `ebt` subsystem.
