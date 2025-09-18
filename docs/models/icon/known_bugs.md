# Known Bugs in ICON

This document collects known build and runtime issues in ICON, including workarounds.
If you encounter a new issue, please add it here so others can avoid debugging it again.

## ecCodes compiles with GCC instead of NVHPC
**Applies to**

- Machine: Balfrin
- Build: ICON compiled without emvorado

**Symptom**

- At runtime, you may see the cryptic error:
```bash
libgomp: TODO
```
or other strange runtime crashes.

**Cause**

- Due to a known bug in ICON’s build system (spack), eccodes is compiled with GCC instead of NVHPC if emvorado is not enabled.

**Workaround / Fix**

- In your spack.yml, explicitly require eccodes to be built with NVHPC:
```bash
- eccodes%nvhpc
```

**Status**

- Known bug. Workaround required. Not yet fixed Spack.