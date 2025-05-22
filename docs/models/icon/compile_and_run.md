# Compile and Run

## Access

The [ICON repository :material-open-in-new:](https://github.com/C2SM/icon){:target="_blank"} is hosted on the C2SM GitHub organisation. If you do not have access, please follow the instructions under [How to get Access](../../about/index.md#how-to-get-access).

  If you do not already have an SSH key set up for GitHub, but would like to do so, follow the [instructions :material-open-in-new:](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent){:target="_blank"}.

Since 2024, ICON is open-source and comes with semi-annual releases, which
can be accessed via [this public repository :material-open-in-new:](https://gitlab.dkrz.de/icon/icon-model){:target="_blank"}.

If you are an ICON developer, you should have access to the DKRZ GitLab, where the original ICON repository is hosted. All developments related to GPU go
into the [`icon-nwp` repository :material-open-in-new:](https://gitlab.dkrz.de/icon/icon-nwp){:target="_blank"}.
    
## Configure and compile

Below you find instructions on how to compile different flavors of ICON on C2SM-supported machines.

Clone the ICON repository:

=== "C2SM (latest release)"
    ```console
    git clone -b release-2025.04 --recurse-submodules git@github.com:C2SM/icon.git
    ```

=== "DKRZ (latest release)"
    ```console
    git clone -b release-2025.04-public --recurse-submodules https://gitlab.dkrz.de/icon/icon-model.git
    ```

=== "DKRZ (icon-nwp master)"
    ```console
    git clone --recurse-submodules git@gitlab.dkrz.de:icon/icon-nwp.git
    ```


### Säntis

!!! info "Last update: 2025-05-22"

    Säntis is regularly maintained by CSCS. In addition, the [uenvs](../../alps/uenvs.md) are updated irregularly. Therefore, some of the information provided here may be out of date. Please use the [C2SM support forum :material-open-in-new:](https://github.com/C2SM/Tasks-Support/discussions){:target="_blank"} in case of questions regarding building ICON on Säntis.

Run the following after navigating into ICON root folder (replace `cpu` by `gpu` if applicable):

```console
UENV_VERSION=$(cat config/cscs/SANTIS_ENV_TAG)
uenv run ${UENV_VERSION} -- ./config/cscs/santis.cpu.nvhpc
```

!!! Note

    For out-of-source builds navigate into the build folder and adapt the path to the configure wrapper above.


### Euler

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


## Run test case
In the *run* folder, you find many prepared test cases, which you can convert into run scripts. To generate the runscript of one of the experiment files, e.g. *c2sm_clm_r13b03_seaice*, you can use the `make_runscripts` function.

```shell
./make_runscripts c2sm_clm_r13b03_seaice
```

To run the created runscript, navigate to the *run* subdirectory and submit the runscript.

=== "Santis"
    ```shell
    UENV_VERSION=$(cat config/cscs/SANTIS_ENV_TAG)
    cd run && sbatch --uenv ${UENV_VERSION} ./exp.c2sm_clm_r13b03_seaice.run
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
