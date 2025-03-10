# Usage

## Access

The [ICON repository :material-open-in-new:](https://github.com/C2SM/icon){:target="_blank"} is hosted on the C2SM GitHub organisation. If you do not have access, please follow the instructions under [How to get Access](../../about/index.md#how-to-get-access).

  If you do not already have an SSH key set up for GitHub, but would like to do so, follow the [instructions :material-open-in-new:](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent){:target="_blank"}.
    
## Configure and compile

### Säntis

!!! construction "Under construction - last update: 2025-02-18"

    Information on this section is not yet complete nor final. It will be updated following the progress of the Alps system deployment at CSCS and C2SM's adaptation to this new system. Please use the [C2SM support forum :material-open-in-new:](https://github.com/C2SM/Tasks-Support/discussions){:target="_blank"} in case of questions regarding building ICON on Alps.

#### ICON at C2SM

Clone the ICON repository on the branch `santis`:
```console
git clone -b santis --recurse-submodules git@github.com:C2SM/icon.git
```

Run the following after navigating into ICON root folder:
```console
# Load ICON user-environment 
uenv start icon-wcp/v1:rc4

# Setup spack
SPACK_TAG=$(cat "config/cscs/SPACK_TAG_ALPS")
git clone --depth 1 --recurse-submodules --shallow-submodules -b ${SPACK_TAG} https://github.com/C2SM/spack-c2sm.git
. spack-c2sm/setup-env.sh /user-environment

# Build ICON
# For out-of-source builds: navigate into the build folder and adapt the path to the Spack environment in the following
spack external find gmake
spack env activate -d config/cscs/spack/${SPACK_TAG}/santis_gpu_nvhpc
spack install
```

#### ICON-NWP

Clone the ICON-NWP repository (only possible if you have access to GitLab DKRZ):
```console
git clone --recurse-submodules git@gitlab.dkrz.de:icon/icon-nwp.git
```

**1. Create a `spack.yaml` file**

Create the following files from the ICON build folder (different to the ICON root folder in case of a out-of-source build). For that, you will have to create the missing folders first:
```bash
SPACK_TAG=$(cat "config/cscs/SPACK_TAG_ALPS")
mkdir -p config/cscs/spack/${SPACK_TAG}/santis_cpu_nvhpc
mkdir -p config/cscs/spack/${SPACK_TAG}/santis_gpu_nvhpc
```

For CPU compilation:

=== "config/cscs/spack/${SPACK_TAG}/santis_cpu_nvhpc/spack.yaml"

  ```yaml
  spack:
    specs:
      - gmake%gcc
      - gnuconfig%gcc
      - cosmo-eccodes-definitions@2.25.0.2
      - icon @develop %nvhpc +grib2 +eccodes-definitions +ecrad ~emvorado +art +dace
        +realloc-buf ~aes ~jsbach ~ocean ~coupling ~rte-rrtmgp
        ~loop-exchange ~async-io-rma
    view: true
    concretizer:
      unify: true
    develop:
      icon:
        path: ../../../../..
        spec: icon @develop %nvhpc +grib2 +eccodes-definitions +ecrad ~emvorado +art
          +dace +realloc-buf ~aes ~jsbach ~ocean
          ~coupling ~rte-rrtmgp ~loop-exchange ~async-io-rma
  ```

For GPU compilation:

=== "config/cscs/spack/${SPACK_TAG}/santis_gpu_nvhpc/spack.yaml"

  ```yaml
  spack:
    specs:
      - gmake%gcc
      - gnuconfig%gcc
      - cosmo-eccodes-definitions@2.25.0.2
      - icon @develop %nvhpc +grib2 +eccodes-definitions +ecrad ~emvorado +art +dace
        gpu=openacc+cuda +mpi-gpu +realloc-buf ~aes ~jsbach ~ocean ~coupling ~rte-rrtmgp
        ~loop-exchange ~async-io-rma ~pgi-inlib +cuda-graphs
    view: true
    concretizer:
      unify: true
    develop:
      icon:
        path: ../../../../..
        spec: icon @develop %nvhpc +grib2 +eccodes-definitions +ecrad ~emvorado +art
          +dace gpu=openacc+cuda +mpi-gpu +realloc-buf ~aes ~jsbach ~ocean
          ~coupling ~rte-rrtmgp ~loop-exchange ~async-io-rma ~pgi-inlib +cuda-graphs
  ```

**2. Build ICON**

Run the following after navigating into the ICON-NWP root folder:
```console
# Load ICON user-environment
uenv start icon-wcp/v1:rc4

# Setup spack
SPACK_TAG=$(cat "config/cscs/SPACK_TAG_ALPS")
git clone --depth 1 --recurse-submodules --shallow-submodules -b ${SPACK_TAG} https://github.com/C2SM/spack-c2sm.git
. spack-c2sm/setup-env.sh /user-environment

# Build ICON
# For out-of-source builds: navigate into the build folder and adapt the path to the Spack environment in the following
spack external find gmake
spack env activate -d config/cscs/spack/${SPACK_TAG}/santis_gpu_nvhpc
spack install
```

### Euler

Clone the ICON repository on the main branch:

```console
git clone --recurse-submodules git@github.com:C2SM/icon.git
```

Load the necessary modules:

```console
module load stack eth_proxy
```

The module `stack` provides the software stack, including `gcc/12.2.0`.
The module `eth_proxy` enables the connection from a compute node to an external service, e.g. GitHub or GitLab.

Run the following after navigating into ICON root folder:

```bash
# Setup spack
SPACK_TAG=$(cat "config/ethz/SPACK_TAG_EULER")
git clone --depth 1 --recurse-submodules --shallow-submodules -b ${SPACK_TAG} https://github.com/C2SM/spack-c2sm.git
. spack-c2sm/setup-env.sh
```

Euler Support recommends to compile code on compute nodes. There,
we can take advantage of multi-core compiling:

```bash
# Build ICON
# For out-of-source builds: navigate into the build folder and 
# adapt the path to the Spack environment in the following
spack env activate -d config/ethz/spack/${SPACK_TAG}/euler_cpu_gcc
srun -N 1 -n 12 --mem-per-cpu=1G spack install -j 12
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
You may need to adjust the account in the runscript to match your permissions. Alternatively, you can include `--account=<my_account_id>` in the `sbatch` command.

!!! info

    The data pool on `santis` is currently not in a persistent location, and you may not have access privileges.
    Therefore, you may not be able to run the test cases at this time.
    As soon as this is fixed, we will update this page accordingly.

## Input data

The input data for standard ICON tests are stored in a [Git-lfs repository :material-open-in-new:](https://gitlab.dkrz.de/icon/testing-input-data){:target="_blank"}.

### Input data pools

=== "Santis"
    ```shell
    /capstor/store/cscs/userlab/d126/pool/data/ICON/
    ```  
=== "Euler"
    ```shell
    /cluster/work/climate/icon_input
    ```
=== "Balfrin"
    ```shell
    /scratch/mch/jenkins/icon/pool/data/ICON
    ```