# Compile and Run

## Access

The [ICON repository :material-open-in-new:](https://github.com/C2SM/icon){:target="_blank"} is hosted on the C2SM GitHub organisation. If you do not have access, please follow the instructions under [How to get Access](../../about/index.md#how-to-get-access).

  If you do not already have an SSH key set up for GitHub, but would like to do so, follow the [instructions :material-open-in-new:](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent){:target="_blank"}.
    
## Configure and compile

### Säntis

!!! construction "Under construction - last update: 2025-04-22"

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

Navigate into the ICON-NWP repository and execute the configure wrapper with the corresponding UENV (replace `cpu` by `gpu` for GPU compilation):
```console
UENV_VERSION=$(cat config/cscs/SANTIS_ENV_TAG)
uenv run ${UENV_VERSION} -- ./config/cscs/santis.cpu.nvhpc
```

### Euler

Clone the ICON repository on the main branch:

```console
git clone --recurse-submodules git@github.com:C2SM/icon.git
```

Run the following after navigating into ICON root folder:

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

```bash
# Build ICON
# For out-of-source builds: navigate into the build folder and 
# adapt the path to the Spack environment in the following
spack env activate -d config/ethz/spack/${SPACK_TAG}/euler_cpu_gcc
srun -N 1 -n 12 --mem-per-cpu=1G spack install -j 12
```


## Run test case
In the *run* folder, you find many prepared test cases, which you can convert into run scripts. To generate the runscript of one of the experiment files, e.g. *c2sm_clm_r13b03_seaice*, you can use the `make_runscripts` function.

```shell
./make_runscripts c2sm_clm_r13b03_seaice
```

To run the created runscript, navigate to the *run* subdirectory and submit the runscript.

=== "Santis"
    ```shell
    cd run && uenv run icon-wcp/v1:rc4 -- sbatch ./exp.c2sm_clm_r13b03_seaice.run
    ```
=== "Euler"
    ```shell
    cd run && sbatch ./exp.c2sm_clm_r13b03_seaice.run
    ```
=== "Balfrin"
    ```shell
    cd run && sbatch ./exp.c2sm_clm_r13b03_seaice.run
    ```
You may need to adjust the account in the runscript to match your permissions. Alternatively, you can include `--account=<my_account_id>` in the `sbatch` command.

## Input data

There are two types in input data sets available for ICON:

- General input data for use cases / production runs
- Testing input data for CI

### Input data pools

=== "Santis"
    ```shell
    /capstor/store/cscs/userlab/cws01/pool/data/ICON
    ```  
=== "Balfrin"
    ```shell
    /scratch/mch/jenkins/icon/pool/data/ICON
    ```
=== "Euler"
    ```shell
    /cluster/work/climate/icon_input
    ```    

### Testing input data pool

The input data for standard ICON tests are stored in a [Git-lfs repository :material-open-in-new:](https://gitlab.dkrz.de/icon/testing-input-data){:target="_blank"}.

=== "Santis"
    ```shell
     /capstor/store/cscs/userlab/d126/testing-input-data
    ```  
=== "Balfrin"
    ```shell
    /scratch/mch/icontest/testing-input-data
    ```
=== "Euler"
    ```shell
    /cluster/work/climate/icon_testing_input
    ```
