# ICON-CLM Workflow

## EURO-CORDEX 12 km

### SPICE

[SPICE](../../tools/spice.md) is a software created by the CLM community and serves as a processing chain / workflow tool
tailored for ICON-CLM simulations.

!!! info

    For a comprehensive overview about SPICE, please consider reading the 
    [official docs :material-open-in-new:](https://hereon-coast.atlassian.net/wiki/spaces/SPICE/pages/983065){:target="_blank"}.

!!! note
    It is assumed that the [uenvs](../../alps/uenvs.md) for ICON and pre-/postprocessing are in place. For that, the following has 
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

#### Get latest SPICE version

Clone SPICE v2.3.1 with the corresponding branch/tag:

```bash
git clone -b v2.3.1 git@github.com:C2SM/spice.git spice
cd spice
```  

#### Configuration

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

#### Get external data

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

#### Clone and build ICON

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

#### Install Python virtual environment

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

#### Option 1) Use Template from C2SM's EURO-CORDEX Run

The official ICON-CLM setups are part of the [spice-setups :material-open-in-new:](https://github.com/C2SM/spice-setups){:target="_blank"} repository.
Please follow the instructions in the [README :material-open-in-new:](https://github.com/C2SM/spice-setups/blob/main/README.md){:target="_blank"} file.


#### Option 2) Manually Create ERA5-driven 12 km case

??? note "Show instructions for manual ERA5-driven case setup"

    From the SPICE root directory, let's create an experiment folder and 
    copy the `sp001` case in there. If you want a different name for your
    experiment, just modify the `EXP` variable.

    !!! note
        The `sp001` is the standard `gcm2icon` test case defined in SPICE.
        It is run on the EURO-CORDEX domain at 44 km horizontal resolution
        and uses ERAInterim data as initial and boundary conditions.
        If you want to run this case, skip the next subsections and continue
        with [Install Python virtual environment](#install-python-virtual-environment).

    ```bash
    EXP=EVAL-EUR12-ERA5
    mkdir -p ${SPICE_DIR}/experiments
    cp -r ${SPICE_DIR}/chain/gcm2icon/sp001 ${SPICE_DIR}/experiments
    mv ${SPICE_DIR}/experiments/sp001 ${SPICE_DIR}/experiments/${EXP}
    ```

    Navigate to the directory where our new case is located:

    ```bash
    cd ${SPICE_DIR}/experiments/${EXP}
    ```

    ##### Adjust boundary data to ERA5

    Since the standard spice case `sp001` takes ERAInterim data as input, 
    we need to replace this with ERA5.

    ```bash
    # Extract lines 17-23 from the source file
    source_lines=$(sed -n '17,23p' ${SPICE_DIR}/chain/boundary_data_options/era5/job_settings)

    # Define job_settings_file
    job_settings_file=${SPICE_DIR}/experiments/${EXP}/job_settings

    # Replace lines 165-173 in the target file with the extracted lines
    sed -i '165,173d' ${job_settings_file}
    line_num=165
    while IFS= read -r line; do
        sed -i "${line_num}i $line" ${job_settings_file}
        line_num=$((line_num + 1))
    done <<< "$source_lines"

    # Replace DKRZ data folder with Alps one
    sed -i 's|/pool/data/CLMcom/CCLM/reanalyses|/capstor/store/cscs/c2sm/c2sme/reanalyses_dkrz|g' ${job_settings_file}
    ``` 

    We also need to replace the `prep` job. This is simply done by copying
    the corresponding file from the boundary data options to our working
    directory:

    ```bash
    cp -v ${SPICE_DIR}/chain/boundary_data_options/era5/prep.job.sh ${SPICE_DIR}/experiments/${EXP}/scripts
    ```

    ##### Adapt `job_settings` file and fix ICON run script

    Now, there are still some necessary adaptations to the `job_settings` file to be done,
    which includes changing paths, ICON executable, meta data and some other settings.

    ```bash
    # General settings
    sed -i "s|icon-nwp|icon-model|g" ${job_settings_file}
    sed -i "s|nco-5.1.9-7pd2hhq2wllvietf2rvclejzxgcjwosq|nco-5.1.9-yykwws3dmcypjzraijgzagmkb6ml2zzo|g" ${job_settings_file}
    sed -i "s|netcdf-c-4.9.2-azccejv4b3ba227zys3e7mkdo6fxxhlq|netcdf-c-4.9.2-5ijnfossknlii33dnqn7asnlmzst3444|g" ${job_settings_file}
    sed -i "s|netcdf-tools/2024:v1-rc1|netcdf-tools/2024:v1|g" ${job_settings_file}
    sed -i "s|EMAIL_ADDRESS= |EMAIL_ADDRESS=michael.jaehn@c2sm.ethz.ch |g" ${job_settings_file}

    # EURO-CORDEX 12 km
    sed -i "s|sp001|${EXP}|g" ${job_settings_file}
    sed -i "s|PFDIR=\${SPDIR}/chain/gcm2icon|PFDIR=\${SPDIR}/experiments|g" ${job_settings_file}
    sed -i "s|WORKDIR=\${SPDIR}/chain|WORKDIR=\${SPDIR}/experiments/work|g" ${job_settings_file}
    sed -i "s|SCRATCHDIR=\${SPDIR}/chain|SCRATCHDIR=\${SPDIR}/experiments/scratch|g" ${job_settings_file}
    sed -i "s|ARCHIVE_OUTDIR=\${SPDIR}/chain|ARCHIVE_OUTDIR=\${SPDIR}/experiments|g" ${job_settings_file}
    sed -i "s|1979-01-01|1940-01-01|g" ${job_settings_file}
    sed -i "s|1979-03-01|2024-01-01|g" ${job_settings_file}
    sed -i "s|europe044|europe011|g" ${job_settings_file}
    sed -i "s|0.44|0.11|g" ${job_settings_file}
    sed -i "s|TIME_ICON=00-00:30:00|TIME_ICON=00-01:00:00|g" ${job_settings_file}
    sed -i "s|TIME_ARCH=\"00-00:30:00\"|TIME_ARCH=\"00-01:30:00\"|g" ${job_settings_file}
    sed -i "s|ITYPE_TS=1|ITYPE_TS=2|g" ${job_settings_file}
    sed -i "s|ITYPE_COMPRESS_POST=0|ITYPE_COMPRESS_POST=1|g" ${job_settings_file}
    sed -i "s|ITYPE_COMPRESS_ARCH=0|ITYPE_COMPRESS_ARCH=1|g" ${job_settings_file}
    sed -i '/ZML_SOIL/c\ZML_SOIL="0.005,0.025,0.07,0.16,0.34,0.7,1.42,2.86,5.74,11.5"    # soil level' ${job_settings_file}
    ```

    For better readability, the following replacements are done:

    **General settings:**

    | Original String                    | Replacement String                              | Description                                  |
    |------------------------------------|-------------------------------------------------|----------------------------------------------|
    | `icon-nwp`                         | `icon-model`                                    | Root directory of ICON model                 |
    | `nco-5.1.9-7pd2hhq2wllvietf2rvclejzxgcjwosq` | `nco-5.1.9-yykwws3dmcypjzraijgzagmkb6ml2zzo` | New nco path due to uenv              |
    | `netcdf-c-4.9.2-azccejv4b3ba227zys3e7mkdo6fxxhlq` | `netcdf-c-4.9.2-5ijnfossknlii33dnqn7asnlmzst3444` | New netcdf path due to uenv |
    | `netcdf-tools/2024:v1-rc1`         | `netcdf-tools/2024:v1`                          | New uenv on santis                           |
    | `EMAIL_ADDRESS= `                  | `EMAIL_ADDRESS=michael.jaehn@c2sm.ethz.ch `     | Add email address for notifications          |

    **EURO-CORDEX 12 km**:

    | Original String                    | Replacement String                              | Description                                  |
    |------------------------------------|-------------------------------------------------|----------------------------------------------|
    | `sp001`                            | `EVAL-EUR12-ERA5`                               | Name of the experiment                       |
    | `PFDIR=${SPDIR}/chain/gcm2icon`    | `PFDIR=${SPDIR}/experiments`                    | Base directory of experiment                 |
    | `WORKDIR=${SPDIR}/chain`           | `WORKDIR=${SPDIR}/experiments/work`             | Working directory of experiment              |
    | `SCRATCHDIR=${SPDIR}/chain`        | `SCRATCHDIR=${SPDIR}/experiments/scratch`       | Scratch directory of experiment              |
    | `ARCHIVE_OUTDIR=${SPDIR}/chain`    | `ARCHIVE_OUTDIR=${SPDIR}/experiments`           | Archive directory of experiment              |
    | `1979-01-01`                       | `1940-01-01`                                    | Start date                                   |
    | `1979-03-01`                       | `2024-01-01`                                    | End date                                     |
    | `europe044`                        | `europe011`                                     | Folder names for ERA5 data                   |
    | `0.44`                             | `0.11`                                          | netCDF metadata for 11 km run                |
    | `TIME_ICON=00-00:30:00`            | `TIME_ICON=00-01:00:00`                         | Increase walltime for icon job               |
    | `TIME_ARCH="00-00:30:00"`          | `TIME_ARCH="00-01:30:00"`                       | Increase walltime for arch job               |
    | `ITYPE_TS=1`                       | `ITYPE_TS=2`                                    | Yearly time series                           |
    | `ITYPE_COMPRESS_POST=0`            | `ITYPE_COMPRESS_POST=1`                         | netCDF compression for post data             |
    | `ITYPE_COMPRESS_ARCH=0`            | `ITYPE_COMPRESS_ARCH=1`                         | netCDF compression for arch data             |
    | `${ICONDIR}/run`                   | `bash ${ICONDIR}/run`                           | Explicitly call bash for the wrapper script  |
    | `ZML_SOIL`                         | `ZML_SOIL=...`                                  | New soil height values                       |

    !!! tip
        There might be even more changes to the `job_settings` file, depending on your setup.
        For example, your CSCS project needs to be set for the `PROJECT_ACCOUNT` variable.
        Also, for production runs, all variables starting with `GA_` should be set accordingly,
        as they are important for the netCDF meta data.

    Furthermore, additional data paths for transient aerosols, ozone and 
    solar irradiation need to be set.

    ```bash
    sed -i '/^TARGET_GRID=/a \
    \
    # Additional directories for aerosol treatment\
    DATADIR_AERO=/capstor/store/cscs/c2sm/c2sme/ICON-CLM/rcm_new\
    \
    KINNE_DIR=${DATADIR_AERO}/europe011/interpolated_aeop_R13B05\
    VOLC_DIR=${DATADIR_AERO}/independent/volcanic_aeropt\
    SP_DIR=${DATADIR_AERO}/independent/MACv2_simple_plumes_merged\
    \
    # Additional directory for ozone treatment\
    OZONE_DIR=${DATADIR_AERO}/europe011/ozone_europe011\
    \
    # Additional directory for solar irradiation\
    SOLAR_DIR=${DATADIR_AERO}/independent/solar_radiation\n' ${job_settings_file}
    ```

    ##### Changing the ICON namelist to match the official CLM configuration

    The official setup can be copied from our `icon-clm_patch` repository, which should already 
    be present in `${SPICE_DIR}/src`.
    This also includes a change for the ICON run script around the `srun` command.

    ```shell
    cp -v ${SPICE_DIR}/src/icon-clm_patch/icon.job.sh ${SPICE_DIR}/experiments/${EXP}/scripts
    cp -v ${SPICE_DIR}/src/icon-clm_patch/post.job.sh ${SPICE_DIR}/experiments/${EXP}/scripts
    ```

    ##### Optional: Warm start run for official ICON-CLM EVAL run

    Replace the ICON run script:

    ```bash
    cp -v ${SPICE_DIR}/src/icon-clm_patch/icon-warm.job.sh ${SPICE_DIR}/experiments/${EXP}/scripts/icon.job.sh
    ```

    It takes the restart file directory (1950/01):

    ```bash
    /capstor/store/cscs/c2sm/c2sme/ICON-CLM/multifile_restart_ATMO_19500101T000000Z.mfr
    ```

    Note that the `START_DATE` in the `job_settings` file needs to be adapted.

#### Run the case

Navigate into your experiment folder and start the simulation chain with

```bash
./subchain start
```

##### `chain_status.log`

The file `chain_status.log` can be inspected at any time and shows the current 
state of the SPICE chain. It contains information about started and finished
jobs.


##### Log files

Job log files are located at `${SPICE_DIR}/experiments/work/${EXP}/joblogs`.


##### Output

Job output files are located at `${SPICE_DIR}/experiments/work/${EXP}/joboutputs`.

##### Restarting the chain

1. Inspect `chain_status.log` to see which job failed.
2. Fix the cause of the problem (e.g., increase walltime for corresponding job in `job_settings`).
3. Check if `date.log` corresponds to the current chunk.
3. Restart the chain by typing `./subchain <jobname>`. If the ICON job failed, use `./subchain icon noprep`.

### EvaSuite

EvaSuite is an addon for SPICE but also a standalone software for either

1. Compare your simulation experiment with E-OBS or ERA5.
2. Compare your simulation experiment and a reference simulation with E-OBS or ERA5.

#### How to use

EvaSuite v1.0 will be released in September 2025. Afterwards, it will be set up on Säntis. 

!!! TODO
    - Install
    - Usage 

### Reference

- [Documentation :material-open-in-new:](https://hereon-coast.atlassian.net/wiki/spaces/SPICE/pages/983091/eva-Suite){:target="_blank"}
- [Repository on GitLab :material-open-in-new:](https://gitlab.dkrz.de/clm-community/evasuite/HZG_Evaluation_Suite){:target="_blank"}

## EURO-CORDEX high-resolution (km-scale)

This will be Phase 2 of the ICON-CLM use case (EXCLAIM). Andreas Prein has
the scientific lead here.
