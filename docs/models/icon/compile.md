# Compile

## Access

Since 2024, ICON is open-source and comes with semi-annual, public releases, which
can be accessed via the public
[icon-model :material-open-in-new:](https://gitlab.dkrz.de/icon/icon-model){:target="_blank"} repository.

If you are an ICON developer, you should have access to the DKRZ GitLab, where the original ICON repository is hosted.
All developments related to GPU porting and NWP settings go
into the [icon-nwp :material-open-in-new:](https://gitlab.dkrz.de/icon/icon-nwp){:target="_blank"} repository.

## Configure and Compile

### Cloning ICON Repository

Below you find instructions on how to compile different flavors of ICON on C2SM-supported machines.

Clone the ICON repository:

=== "Latest release at DKRZ GitLab"
    ```console
    git clone -b release-2026.10-public --recurse-submodules https://git.gitlab.dkrz.de/icon/icon-model.git
    ```

=== "icon-nwp master branch at DKRZ GitLab"
    ```console
    git clone --recurse-submodules git@git.gitlab.dkrz.de:icon/icon-nwp.git
    ```

### Compiling

#### Säntis

Run the following after navigating into the ICON root folder:

=== "CPU compilation"
    ```console
    UENV_VERSION=$(cat config/cscs/SANTIS_ENV_TAG)
    uenv run ${UENV_VERSION} --view default -- ./config/cscs/santis.cpu.nvhpc
    ```

=== "GPU compilation"
    ```console
    UENV_VERSION=$(cat config/cscs/SANTIS_ENV_TAG)
    uenv run ${UENV_VERSION} --view default -- ./config/cscs/santis.gpu.nvhpc
    ```

!!! info "User environments (uenvs)"

    If you have never used a uenv on Säntis, you need to create a uenv repo first:
    ```
    uenv repo create
    ```

    In case you are using the uenv version for the first time, you need to pull the image first:
    ```
    uenv image pull $UENV_VERSION
    ```

##### Building out-of-source

Out-of-source builds are useful if you want to have two or more compiled versions of ICON in the same repository.
To achieve that, you simply need to create separate folders in the ICON root folder
and run the configure wrapper from there.

For example, if you want to compile ICON both for `cpu` and `gpu`, create those directories:

```bash
mkdir nvhpc_cpu
mkdir nvhpc_gpu
```

Then, navigate into the corresponding folder and source the configure wrapper for compilation:

=== "`cpu`"
    ```bash
    UENV_VERSION=$(cat config/cscs/SANTIS_ENV_TAG)
    cd nvhpc_cpu
    uenv run ${UENV_VERSION} --view default -- ./../config/cscs/santis.cpu.nvhpc
    ```
=== "`gpu`"
    ```bash
    UENV_VERSION=$(cat config/cscs/SANTIS_ENV_TAG)
    cd nvhpc_gpu
    uenv run ${UENV_VERSION} --view default -- ./../config/cscs/santis.gpu.nvhpc
    ```

#### Balfrin

Run the following after navigating into the ICON root folder:

=== "CPU compilation"
    ```console
    ./config/cscs/alps_mch.cpu.nvidia
    ```

=== "GPU compilation"
    ```console
    ./config/cscs/alps_mch.gpu.nvidia
    ```

You can run the above scripts out-of-source also.

#### Eiger

Pull and start the Environment:

```bash
uenv image pull prgenv-gnu/24.11:v1
uenv start --view=spack prgenv-gnu/24.11:v1
```

Clone and setup Spack

```bash
git clone -b releases/v0.23 https://github.com/spack/spack
source spack/share/spack/setup-env.sh
```

Set spack system config path:

```bash
export SPACK_SYSTEM_CONFIG_PATH=/user-environment/config/
```

Modify compiler flags for ICON:

Edit the file: `spack/var/spack/repos/builtin/packages/icon/package.py`

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

Create and configure Spack environment for ICON

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

Activate the environment:

```bash
spack env activate path/to/my-icon
```

Concretize and install packages:

```bash
spack concretize
spack install
```

`concretize` resolves dependencies, and `install` builds the packages.

#### Euler

Navigate into the ICON root folder.

Now, set up your spack instance:

```bash
# Setup spack
SPACK_TAG=$(cat "config/ethz/SPACK_TAG_EULER")
git clone --depth 1 --recurse-submodules --shallow-submodules -b ${SPACK_TAG} https://github.com/C2SM/spack-c2sm.git
. spack-c2sm/setup-env.sh
```

Euler Support recommends to compile code on compute nodes. There,
we can take advantage of multi-core compiling.
However, we need to load the module `eth_proxy`, which enables connecting from a compute node
to an external service, e.g. GitHub or GitLab.

```console
module load eth_proxy
```

Now, activate the spack environment and build ICON:

```bash
# Build ICON
# For out-of-source builds: navigate into the build folder and 
# adapt the path to the Spack environment in the following
spack env activate -d config/ethz/spack/${SPACK_TAG}/euler_cpu_gcc
srun -N 1 -n 12 --mem-per-cpu=1G spack install -j 12
```

## Compile Options

On all machines above, ICON is built with [Spack :material-open-in-new:](https://spack.readthedocs.io){:target="_blank"}.
The ICON configuration is defined by the Spack spec in the `spack.yaml` file of the environment
that the configure wrapper activates:

| Machine | Configure wrapper | Spack environment |
| --- | --- | --- |
| Säntis | `config/cscs/santis.cpu.nvhpc` | `config/cscs/spack/santis_cpu_double` |
| Säntis | `config/cscs/santis.gpu.nvhpc` | `config/cscs/spack/santis_gpu_double` |
| Balfrin | `config/cscs/alps_mch.cpu.nvidia` | `config/cscs/spack/mch_cpu_double` |
| Balfrin | `config/cscs/alps_mch.gpu.nvidia` | `config/cscs/spack/mch_gpu_double` |
| Euler | `config/ethz/euler.cpu.gcc` | `config/ethz/spack/euler_cpu_gcc` |

A spec looks like this (example for Säntis CPU):

```yaml
spack:
  specs:
    - icon-nwp @develop +grib2 +eccodes-definitions +ecrad +art ~aes
      ~jsbach ~ocean ~coupling ~rte-rrtmgp ~loop-exchange +mpi %c,cxx,fortran=nvhpc
```

### Enable or Disable Components

Each `+<variant>` enables and each `~<variant>` disables a feature, which translates to
`--enable-<variant>` and `--disable-<variant>` of the ICON `configure` script.
For example, to build ICON with the ICON community interface (ComIn) but without ART, change the spec to:

```yaml
    - icon-nwp @develop +grib2 +eccodes-definitions +ecrad ~art +comin ~aes
      ~jsbach ~ocean ~coupling ~rte-rrtmgp ~loop-exchange +mpi %c,cxx,fortran=nvhpc
```

Then rerun the configure wrapper as described above. Spack detects the modified spec and rebuilds ICON.

To list all available variants and their default values, run the following
with the Spack instance of your build loaded:

```console
spack info icon-nwp
```

!!! info "Package name"
    Depending on the ICON version and the machine, the spec uses either the `icon` or the `icon-nwp`
    Spack package. Use the package name of your `spack.yaml` file for `spack info`.

Configure options without a corresponding variant can be passed with the `extra-config-args` variant
of `icon-nwp`, e.g., `extra-config-args=--enable-dim-swap`.
Use this cautiously, as it bypasses the consistency checks of the Spack package.

### Change Compiler Flags

Additional compiler flags are set with the `fflags` (Fortran), `cflags` (C), and `ldflags` (linker)
variants. They are appended to the default flags of the Spack package. For example, to obtain
debug information and a traceback when the model crashes:

```yaml
    - icon-nwp @develop +grib2 +eccodes-definitions +ecrad +art ~aes
      ~jsbach ~ocean ~coupling ~rte-rrtmgp ~loop-exchange +mpi
      fflags="-g -traceback" %c,cxx,fortran=nvhpc
```

!!! warning "Check that your flags are applied"
    These variants only reach the compiler with a spack-c2sm version that includes
    [C2SM/spack-c2sm#1089 :material-open-in-new:](https://github.com/C2SM/spack-c2sm/pull/1089){:target="_blank"}.
    Older versions silently ignore them. Check the `FCFLAGS` entry in the `config.log` file
    of your build folder to verify which flags are used.

To compile a subset of the source code with a different flag, e.g., a lower optimization level for
a part that causes problems, use the `fcgroup` variant of `icon-nwp` with the format `NAME.paths.flag`:

```yaml
fcgroup=NWP.src/atm_phy_nwp.-O1
```

`NAME` consists of capital letters, `paths` is a colon-separated list of files and directories
relative to the ICON root folder (without dots), and `flag` is a single compiler flag that is used
instead of the default `ICON_FCFLAGS` for these files.

### Recommendations

- **Compile only what you need:** Disable all components that your experiment does not use
  (e.g., `~ocean ~jsbach ~coupling ~waves ~art`). This reduces the compilation time and the number of
  dependencies that may fail to build.
- **Use one build folder per configuration:** Combine different specs with
  [out-of-source builds](#building-out-of-source) instead of recompiling the same folder.
- **Keep debug and production builds apart:** Debug flags such as `-g` or `-O0` slow down the model
  considerably. Do not use them for production runs.
- **Keep track of your changes:** The `spack.yaml` files are part of the ICON repository.
  Commit your modifications to your own branch so that the configuration of your build is reproducible.
