# Eiger

Eiger is an Alps cluster that provides compute nodes and file systems designed to meet the needs
of CPU-only workloads for the HPC Platform. For more information, please refer to the
[CSCS Documentation :material-open-in-new:](https://docs.cscs.ch/clusters/eiger/){:target="_blank"}.

C2SM only provides partial support for Eiger. Nevertheless, below you can find instructions on how
to set up ICON on Eiger.

## Setting Up ICON with Spack on Eiger

### 1. Pull and Start the Environment

```bash
uenv image pull prgenv-gnu/24.11:v1
uenv start --view=spack prgenv-gnu/24.11:v1
```

### 2. Clone and Setup Spack

```bash
git clone -b releases/v0.23 https://github.com/spack/spack
source spack/share/spack/setup-env.sh
```

Set spack system config path:

```bash
export SPACK_SYSTEM_CONFIG_PATH=/user-environment/config/
```


### 3. Modify Compiler Flags for ICON

Edit the file: `spack/var/spack/repos/builtin/packages/icon/package.pypackages.py`

Add the following under the line `if self.compiler.name == "gcc":`:

```python
flags["LDFLAGS"].append("-Wl,--copy-dt-needed-entries")
flags["ICON_FCFLAGS"].append("-fallow-argument-mismatch")
flags["ICON_OCEAN_FCFLAGS"].extend([
    "-O3",
    "-fno-tree-loop-vectorize",
    "-fallow-argument-mismatch"
])
```

### 4. Create and Configure Spack Environment for ICON

```bash
spack env create my-icon
```

Modify the `spack.yaml` file in your `my-icon` environment. Example:

```yaml
# This is a Spack Environment file.
#
# It describes a set of packages to be installed, along with
# configuration settings.
spack:
  specs:
  - icon+art+rte-rrtmgp+grib2 -ocean ~coupling
  view: true
  concretizer:
    unify: true
  develop:
    icon:
      spec: icon +rte-rrtmgp +art +grib2 -ocean ~coupling
      path: /capstor/store/cscs/empa/em05/ckeller/icon-kit
  compilers:
  - compiler:
      spec: gcc@=7.5.0
      paths:
        cc: /usr/bin/gcc
        cxx: /usr/bin/g++
        f77: /usr/bin/gfortran
        fc: /usr/bin/gfortran
      flags: {}
      operating_system: sles15
      target: x86_64
      modules: []
      environment: {}
      extra_rpaths: []
  - compiler:
      spec: gcc@=12.3.0
      paths:
        cc: /usr/bin/gcc-12
        cxx: /usr/bin/g++-12
        f77: /usr/bin/gfortran-12
        fc: /usr/bin/gfortran-12
      flags: {}
      operating_system: sles15
      target: x86_64
      modules: []
      environment: {}
      extra_rpaths: []
```

!!! warning "Path to ICON code"
    Ensure `develop.icon.path` points to your local ICON source code.

### 5. Activate the Environment

```bash
spack env activate path/to/my-icon
```

### 6. Concretize and Install Packages

```bash
spack concretize
spack install
```

`concretize` resolves dependencies, and `install` builds the packages.