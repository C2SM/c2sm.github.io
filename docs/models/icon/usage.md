# Usage

## Access

The [ICON repository :material-open-in-new:](https://github.com/C2SM/icon){:target="_blank"} is hosted on the C2SM GitHub organisation. If you do not have access, please follow the instructions under [How to get Access](../../about/index.md#how-to-get-access).

Once you have access, clone the repository from GitHub using the SSH protocol:

  ```bash
  git clone --recurse-submodules git@github.com:C2SM/icon.git
  ```
  If you do not already have an SSH key set up for GitHub, but would like to do so, follow the [instructions :material-open-in-new:](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent){:target="_blank"}.
    
## Configure and compile

### Säntis

!!! construction "Under construction - last update: 2024-12-18"

    Information on this section is not yet complete nor final. It will be updated following the progress of the Alps system deployment at CSCS and C2SM's adaptation to this new system. Please use the [C2SM support forum :material-open-in-new:](https://github.com/C2SM/Tasks-Support/discussions){:target="_blank"} in case of questions regarding building ICON on Alps.

Currently, the same ICON user environment used on `todi` is being used. Since the environment is still linked to `todi`, you need to export the `CLUSTER_NAME` to `todi` for now:

```bash
export CLUSTER_NAME=todi
```

Next, follow the instructions to build ICON using Spack below.

**1. Create a `spack.yaml` file**

Create the following files from the ICON build folder (different to the ICON root folder in case of a out-of-source build). For that, you will have to create the missing folders first:
```bash
mkdir -p config/cscs/spack/v0.21.1.3/alps_cpu_nvhpc
mkdir -p config/cscs/spack/v0.21.1.3/alps_gpu_nvhpc
```

For CPU compilation:

=== "config/cscs/spack/v0.21.1.3/alps_cpu_nvhpc/spack.yaml"

  ```yaml
  spack:
    specs:
      - cosmo-eccodes-definitions@2.25.0.2
      - icon @develop %nvhpc +grib2 +eccodes-definitions +ecrad ~emvorado +art +dace +acm-license ~aes ~jsbach ~ocean ~coupling ~rte-rrtmgp ~loop-exchange ~async-io-rma +pgi-inlib
    view: true
    concretizer:
      unify: when_possible
    develop:
      icon:
        path: ../../../../..
        spec: icon @develop %nvhpc +grib2 +eccodes-definitions +ecrad ~emvorado +art +dace +acm-license ~aes ~jsbach ~ocean ~coupling ~rte-rrtmgp ~loop-exchange ~async-io-rma +pgi-inlib
  ```

For GPU compilation:

=== "config/cscs/spack/v0.21.1.3/alps_gpu_nvhpc/spack.yaml"

  ```yaml
  spack:
    specs:
      - cosmo-eccodes-definitions@2.25.0.2
      - icon @develop %nvhpc +grib2 +eccodes-definitions +ecrad ~emvorado +art +dace +acm-license gpu=openacc+cuda +mpi-gpu +realloc-buf ~aes ~jsbach ~ocean ~coupling ~rte-rrtmgp ~loop-exchange ~async-io-rma +pgi-inlib +cuda-graphs
    view: true
    concretizer:
      unify: when_possible
    develop:
      icon:
        path: ../../../../..
        spec: icon @develop %nvhpc +grib2 +eccodes-definitions +ecrad ~emvorado +art +dace +acm-license gpu=openacc+cuda +mpi-gpu +realloc-buf ~aes ~jsbach ~ocean ~coupling ~rte-rrtmgp ~loop-exchange ~async-io-rma +pgi-inlib +cuda-graphs
  ```

**2. Build ICON**

Run the following from the ICON root folder:
```console
# Load ICON user-environment 
uenv start --view=spack icon-wcp/v1:rc4

# Setup spack
SPACK_TAG='v0.21.1.3'
git clone --depth 1 --recurse-submodules --shallow-submodules -b ${SPACK_TAG} https://github.com/C2SM/spack-c2sm.git
. spack-c2sm/setup-env.sh /user-environment

# Build ICON
cd /path/to/icon-build-folder
spack env activate -d config/cscs/spack/${SPACK_TAG}/alps_gpu_nvhpc
spack install
```

### Euler
Spack is used to build ICON. Please follow the steps below to set up Spack and build ICON.

**1. Set up a Spack instance**

To [set up a Spack instance :material-open-in-new:](https://c2sm.github.io/spack-c2sm/latest/QuickStart.html#at-cscs-daint-tsa-balfrin){:target="_blank"}, ensure that you clone the repository using the Spack tag provided in the ICON repository at [config/ethz/SPACK_TAG_EULER :material-open-in-new:](https://github.com/C2SM/icon/blob/main/config/ethz/SPACK_TAG_EULER){:target="_blank"} and load it into your command line.


**2. Build ICON**

Activate the Spack environment for Euler:
```bash
SPACK_TAG=$(cat "config/ethz/SPACK_TAG_EULER")
spack env activate -d config/ethz/spack/$SPACK_TAG/euler_cpu_gcc
```

Euler Support recommends to compile code on compute-nodes. Unfortunately [internet-access on Euler compute-nodes is restricted :material-open-in-new:](https://scicomp.ethz.ch/wiki/Accessing_the_clusters#Internet_Security){:target="_blank"}.
Therefore a two-step install needs to be performed:

```bash
# fetch and install cosmo-eccodes-definitions on login-node
spack install cosmo-eccodes-definitions

# compile ICON on compute-nodes
srun -N 1 -c 12 --mem-per-cpu=20G spack install -v -j 12
```

### Piz Daint
Spack is used to build ICON. Please follow the steps below to set up Spack and build ICON.

**1. Set up a Spack instance**

To [set up a Spack instance :material-open-in-new:](https://c2sm.github.io/spack-c2sm/latest/QuickStart.html#at-cscs-daint-tsa-balfrin){:target="_blank"}, ensure that you clone the repository using the Spack tag provided in the ICON repository at [config/cscs/SPACK_TAG_C2SM :material-open-in-new:](https://github.com/C2SM/icon/blob/main/config/cscs/SPACK_TAG_C2SM){:target="_blank"} and load it into your command line.

**2. Build ICON**

Refer to the official spack-c2sm documentation for [installing ICON using Spack :material-open-in-new:](https://c2sm.github.io/spack-c2sm/latest/QuickStart.html#icon){:target="_blank"}.

After the first compilation, you need to create a `setting` file (the following example is for Piz Daint, please adapt the lines according to the machine you are using):

=== "daint_gpu_nvhpc"
    ```shell
    # Get SPACK_TAG used on machine
    SPACK_TAG=$(cat "config/cscs/SPACK_TAG_C2SM")
    # Set the name of the environment, which should be equal to the builder
    ENV_NAME=daint_gpu_nvhpc
    # Load probtest environment (only needed if you want to run check files)
    source /project/g110/icon/probtest/conda/miniconda/bin/activate probtest
    # Ensure CDO is loaded on your machine
    module load daint-gpu CDO
    # Remove and create setting file with the following two commands
    rm -f setting
    ./config/cscs/create_sh_env $SPACK_TAG $ENV_NAME
    ```

## Run test case
In the *run* folder, you find many prepared test cases, which you can convert into run scripts. To generate the runscript of one of the experiment files, e.g. *mch_ch_lowres*, you can use the `make_runscripts` function.

```bash
./make_runscripts mch_ch_lowres
```

To run the created runscript, navigate to the *run* subdirectory and submit the runscript.

```bash
cd run && sbatch ./exp.mch_ch_lowres.run
```
You may need to adjust the account in the runscript to match your permissions. Alternatively, you can include `--account <my_account_id>` in the `sbatch` command.

## Input data
ICON input data are stored at the following locations:

- **Piz Daint (CSCS):** `/users/icontest/pool/data/ICON`
- **Euler:** `/cluster/work/climate/icon_input`

