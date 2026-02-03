# ICON-CLM Workflow for EURO-CORDEX 12 km Domain

## SPICE

[SPICE](../../tools/spice.md) is a software created by the CLM community and serves as a processing chain / workflow tool
tailored for ICON-CLM simulations.

!!! info

    For a comprehensive overview about SPICE, please consider reading the 
    [official docs :material-open-in-new:](https://hereon-coast.atlassian.net/wiki/spaces/SPICE/pages/983065){:target="_blank"}.

!!! note
    It is assumed that the [uenvs](../../hpc/index.md#user-environments) for ICON and pre-/postprocessing are in place. For that, the following has 
    to be executed once:

    ```bash
    uenv repo create
    uenv image pull icon-wcp/v1:rc4
    uenv image pull netcdf-tools/2024:v1
    ```

    Be sure that `CLUSTER_NAME=todi` is **not** present anywhere (e.g. in your `~/.bashrc`) as it is not needed anymore.
    The two uenvs we need are available on santis.

    For more information about uenvs, see [the CSCS documentation :material-open-in-new:](https://docs.cscs.ch/software/uenv){:target="_blank"}.

Load the `netcdf-tools` uenv:

```bash
uenv start --view=modules netcdf-tools/2024:v1
```

### Get latest SPICE version

Clone SPICE v2.3.1 with the corresponding branch/tag:

```bash
git clone -b v2.3.1 git@github.com:C2SM/spice.git spice
cd spice
```  

### Configuration

First, set the `SPICE_DIR` environment variable as it will be needed later on:

```bash
SPICE_DIR=$(pwd)
```

Alps is officially supported in SPICE >=v2.3 and can be configured in the following way:

```bash
./test/cscs-alps/scripts/configure.sh
```

!!! note
    All scripts in `test/cscs-alps/scripts` are wrapper scripts to facilitate the build
    and configure process on Alps. If something should be done in a different way,
    check the contents of the scripts and modify them accordingly or configure and
    build the software manually according to the
    [SPICE Docs :material-open-in-new:](https://hereon-coast.atlassian.net/wiki/spaces/SPICE/pages/983065/Install){:target="_blank"}.

### Get external data

The standard SPICE configuration needs ERAInterim or ERA5 data and initial
and boundary conditions.
This is originally provided on Levante@DKRZ. For Alps, the data is also 
synced to this destination:

```shell
/capstor/store/cscs/c2sm/c2sme/reanalyses_dkrz
``` 

For reference, check the information about
[ERA5 :material-open-in-new:](https://c2sm.github.io/datasets/obs_reanalysis_data/#era5-for-icon-clm){:target="_blank"}
and [ERAInterim :material-open-in-new:](https://c2sm.github.io/datasets/obs_reanalysis_data/#erainterim){:target="_blank"}
datasets.

Additionally, external parameters on the ICON grids (44 km and 11 km available)
and supplemental data for the radiation module (e.g. greenhouse gas time series)
are provided by DKRZ. This data needs to be downloaded:

```bash
./test/cscs-alps/scripts/get-data.sh
```

The data is then available under `data/rcm`.

### Clone and build ICON

First, we will clone the official ICON release 2024.07:

```bash
./test/cscs-alps/scripts/clone-icon.sh icon-model
```

The positional parameter `icon-model` ensures that the official release is pulled.
If omitted, the latest version of `icon-nwp` (requires access and an SSH key to
[https://gitlab.dkrz.de :material-open-in-new:](https://gitlab.dkrz.de){:target="_blank"}) is used.

The GPU version of ICON v2024.07 does not contain all namelist features for the
ICON-CLM setup. Hence, we apply a [patch with the missing GPU ports :material-open-in-new:](https://github.com/C2SM/icon-clm_patch){:target="_blank"}.
This is already part of the `clone-icon.sh` script.

Before we can build ICON, we need to set up our spack instance:

```bash
./test/cscs-alps/scripts/setup-spack.sh icon-model
```

Now, switch to another terminal to build ICON using the corresponding uenv:

=== "uenv: icon-wcp/v1:rc4"

    ```bash
    uenv start icon-wcp/v1:rc4
    ./test/cscs-alps/scripts/build-icon.sh gpu icon-model
    ```

Afterwards, go back to your original terminal containing the 
`netcdf-tools/2024:v1` uenv.

### Install Python virtual environment

Some scripts in SPICE use Python. For that, some dependencies have to be installed.

**Step 1: Download and Install Miniforge**

```bash
wget https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-aarch64.sh
bash Miniforge3-Linux-aarch64.sh
source ~/miniforge3/bin/activate
```

**Step 2: Create a conda virtual environment**

```bash
conda create --prefix ${SPICE_DIR}/venv python=3.12 -y
conda activate ${SPICE_DIR}/venv 
```

**Step 3: Install packages**

```bash
conda install pip -y
pip install -r requirements.txt
```

**Step 4: Verify installation**

```bash
${SPICE_DIR}/venv/bin/python -c 'import xarray; import pandas; import numpy; import scipy; import h5netcdf; import matplotlib; import cftime; import netCDF4; print("All modules imported successfully!")'
```
Now your Python environment for SPICE is ready to go! 🚀

### Use Experiment Template from C2SM's EURO-CORDEX Run 

The official ICON-CLM setups are part of the [spice-setups :material-open-in-new:](https://github.com/C2SM/spice-setups){:target="_blank"} repository.
Please follow the instructions in the [README :material-open-in-new:](https://github.com/C2SM/spice-setups/blob/main/README.md){:target="_blank"} file.


### Run the case

Navigate into your experiment folder and start the simulation chain with

```bash
./subchain start
```

#### `chain_status.log`

The file `chain_status.log` can be inspected at any time and shows the current 
state of the SPICE chain. It contains information about started and finished
jobs.


#### Log files

Job log files are located at `${SPICE_DIR}/experiments/work/${EXP}/joblogs`.


#### Output

Job output files are located at `${SPICE_DIR}/experiments/work/${EXP}/joboutputs`.

#### Restarting the chain

1. Inspect `chain_status.log` to see which job failed.
2. Fix the cause of the problem (e.g., increase walltime for corresponding job in `job_settings`).
3. Check if `date.log` corresponds to the current chunk.
3. Restart the chain by typing `./subchain <jobname>`. If the ICON job failed, use `./subchain icon noprep`.


