# HxS PackageTracker

the HxS PackageTracker is a collection of `ebs(5)` formulae, designed to be built to assemble a complete HxS system.

## formulae

- `shush`: the SHUSH shell
- `xpt`: the XPT package manager
- `hbase`: the HBASE utility collection
- `xpt.static`: static, minimal builds of XPT
- `shush.static`: static, minimal builds of SHUSH

### how to build

each formula can be built with:

```sh
ebs build package/package-version.ebs
```

> the `ebs(1)` build system can be found as a shell script in the `xpt` package, as part of the `ebt` subsystem.
