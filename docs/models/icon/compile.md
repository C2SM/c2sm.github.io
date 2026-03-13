# Compile

## Access

Since 2024, ICON is open-source and comes with semi-annual, public releases, which
can be accessed via the public [icon-model :material-open-in-new:](https://gitlab.dkrz.de/icon/icon-model){:target="_blank"} repository.

If you are an ICON developer, you should have access to the DKRZ GitLab, where the original ICON repository is hosted. All developments related to GPU porting and NWP settings go
into the [icon-nwp :material-open-in-new:](https://gitlab.dkrz.de/icon/icon-nwp){:target="_blank"} repository.
    
## Configure and Compile

### Cloning ICON Repository

Below you find instructions on how to compile different flavors of ICON on C2SM-supported machines.

Clone the ICON repository:

=== "Latest release at DKRZ GitLab"
    ```console
    git clone -b release-2025.10-public --recurse-submodules https://gitlab.dkrz.de/icon/icon-model.git
    ```

=== "icon-nwp master branch at DKRZ GitLab"
    ```console
    git clone --recurse-submodules git@gitlab.dkrz.de:icon/icon-nwp.git
    ```

### Compiling

#### Säntis

!!! info "Changes needed for latest ICON release"
    Before continuing with the instructions below, you must apply the following patch if you are using the latest DKRZ GitLab release `2025.10` (older releases have not been tested). The same applies if you are using an `icon-nwp` version prior to the [[hotfix] Fix CI after major update of Säntis :material-open-in-new:](https://gitlab.dkrz.de/icon/icon-nwp/-/commit/2d6ef79e184af8cce957f8b6862f076040285c62){:target="_blank"} commit.
    <details>
    <summary> <b><u> patch </u></b> </summary>

    ```diff
    diff --git a/config/cscs/SANTIS_ENV_TAG b/config/cscs/SANTIS_ENV_TAG
    index 4b8589c5a..f4526e9f3 100644
    --- a/config/cscs/SANTIS_ENV_TAG
    +++ b/config/cscs/SANTIS_ENV_TAG
    @@ -1 +1 @@
    -icon/25.2:v3
    +icon/25.2:v4
    diff --git a/config/cscs/spack/santis_cpu_double/spack.yaml b/config/cscs/spack/santis_cpu_double/spack.yaml
    index f0300a1b9..20c7ce662 100644
    --- a/config/cscs/spack/santis_cpu_double/spack.yaml
    +++ b/config/cscs/spack/santis_cpu_double/spack.yaml
    @@ -11,8 +11,11 @@
     spack:
       specs:
       - cosmo-eccodes-definitions@2.36.0.3
    -  - icon @develop %nvhpc +grib2 +eccodes-definitions +ecrad +emvorado +art +dace ~aes
    -    ~jsbach ~ocean ~coupling ~rte-rrtmgp ~loop-exchange
    +  - icon @develop %nvhpc +grib2 +eccodes-definitions +ecrad +emvorado +art ~aes
    +    ~jsbach ~ocean ~coupling ~rte-rrtmgp ~loop-exchange +mpi
       view: true
       concretizer:
         unify: true
    +  packages:
    +    mpi:
    +      require: cray-mpich%nvhpc
    diff --git a/config/cscs/spack/santis_gpu_double/spack.yaml b/config/cscs/spack/santis_gpu_double/spack.yaml
    index 677e1bd3b..052d0856a 100644
    --- a/config/cscs/spack/santis_gpu_double/spack.yaml
    +++ b/config/cscs/spack/santis_gpu_double/spack.yaml
    @@ -11,9 +11,12 @@
     spack:
       specs:
       - cosmo-eccodes-definitions@2.36.0.3
    -  - icon @develop %nvhpc +grib2 +eccodes-definitions +ecrad +emvorado +art +dace gpu=nvidia-90
    +  - icon @develop %nvhpc +grib2 +eccodes-definitions +ecrad +emvorado +art gpu=nvidia-90
         +mpi-gpu +realloc-buf ~aes ~jsbach ~ocean ~coupling ~rte-rrtmgp ~loop-exchange
         ~cuda-graphs fflags="-traceback"
       view: true
       concretizer:
         unify: true
    +  packages:
    +    mpi:
    +      require: cray-mpich%nvhpc
    ```

    </details>

Run the following after navigating into the ICON root folder:

=== "CPU compilation"
    ```console
    UENV_VERSION=$(cat config/cscs/SANTIS_ENV_TAG)
    uenv run ${UENV_VERSION} -- ./config/cscs/santis.cpu.nvhpc
    ```

=== "GPU compilation"
    ```console
    UENV_VERSION=$(cat config/cscs/SANTIS_ENV_TAG)
    uenv run ${UENV_VERSION} -- ./config/cscs/santis.gpu.nvhpc
    ```

!!! info "User environments and out-of-source builds"

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
    uenv run ${UENV_VERSION} -- ./../config/cscs/santis.cpu.nvhpc 
    ```
=== "`gpu`"
    ```bash
    UENV_VERSION=$(cat config/cscs/SANTIS_ENV_TAG)
    cd nvhpc_gpu
    uenv run ${UENV_VERSION} -- ./../config/cscs/santis.gpu.nvhpc 
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
