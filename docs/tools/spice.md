
# SPICE

SPICE stands for **S**tarter **P**ackage for **I**CON-**C**LM **E**xperiments. It is a processing chain that handles pre-processing of the input,
setting up namelists, running the simulation and archiving/post-processing. It contains the latest setup for ICON-CLM
runs by the CLM community.

The code has been adapted for running on Alps and can be downloaded via [Zenodo :material-open-in-new:](https://zenodo.org/records/10047021){:target="_blank"}.

To set up your own ICON-CLM simulation, refer to the [corresponding ICON page](../models/icon/icon-clm.md).

For any questions, please contact [Michael Jähn :material-open-in-new:](https://c2sm.ethz.ch/the-center/people/person-detail.html?persid=286091){:target="_blank"}.

## Code

* [SPICE source code (public) :material-open-in-new:](https://gitlab.dkrz.de/clm-community/public/spice){:target="_blank"} 

## Documentation

* [SPICE Docs :material-open-in-new:](https://spice.clm-community.eu/){:target="_blank"}


## EvaSuite

EvaSuite is an addon for SPICE but also a standalone software for either

1. Compare your simulation experiment with E-OBS or ERA5.
2. Compare your simulation experiment and a reference simulation with E-OBS or ERA5.

### Instructions to Set Up on Säntis

!!! warning "Instructions partly outdated"

    Due to the latest updates of EvaSuite, there is no official support on Santis.
    The instructions below may still be valid, but could also be partly outdated.
    In any case, please refer to the official EvaSuite Documentation.

#### Setup Miniforge

EvaSuite needs a conda environment setup to run properly. On a HPC system as Alps/Säntis,
Conda's packages and environments should be installed on `$SCRATCH` in order to not run into the file quota limit.
Miniforge itself can be installed in `$HOME`.

**Download Miniforge for aarch64**

```bash
cd ~
wget https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-aarch64.sh
```

**Install Miniforge into your home directory**

```bash
Miniforge3-Linux-aarch64.sh -b -p $HOME/miniforge3
```

**Add Miniforge to your PATH**

```bash
echo 'export PATH=$HOME/miniforge3/bin:$PATH' >> ~/.bashrc
```

**Configure Conda to store envs/pkgs on `$SCRATCH`**

Create `~/.condarc`:

```yaml
channels:
  - conda-forge
channel_priority: strict

envs_dirs:
  - $SCRATCH/conda_envs
pkgs_dirs:
  - $SCRATCH/conda_pkgs

auto_activate_base: false
```

uenv and modules:

```bash
uenv start --view=modules netcdf-tools/2024:v1
module load gcc/13.2.0 hdf5/1.14.3
``` 

Base environment:

```bash
conda create -n py310_evasuite python=3.10 -y
conda activate py310_evasuite
```

Installing packages:

```bash
conda install -c conda-forge fiona cartopy rasterio h5py psutil
```

#### Installation

Follow `DOCS/installation.md`:

1. **Clone the repository**
```bash
git clone --recurse-submodules https://gitlab.dkrz.de/clm-community/public/evasuite.git EvaSuite_v1.0
```



2. **Create and activate a Python virtual environment within the EvaSuite repo**
```bash
cd EvaSuite_v1.0
conda activate py310_evasuite
```

3. **Tell pip to Use `$SCRATCH` for Cache & Wheels**

```bash
export PIP_CACHE_DIR=$SCRATCH/pip_cache
export TMPDIR=$SCRATCH/pip_temp
mkdir -p $PIP_CACHE_DIR $TMPDIR
```

4. **Upgrade pip and install dependencies**
```bash
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

5. **Install EvaSuite**
```bash
pip install .
```


### Usage

Load modules and activate environment:
```bash
uenv start --view=modules netcdf-tools/2024:v1
module load cdo/2.4.0 netcdf-c/4.9.2 netcdf-fortran/4.6.1
conda activate py310_evasuite
```

### Reference

- [PDF Documentation :material-open-in-new:](https://gitlab.dkrz.de/clm-community/public/evasuite/-/raw/main/DOCS/Documentation_EvaSuite_v1_0.pdf?ref_type=heads&inline=true){:target="_blank"}
- [EvaSuite within SPICE User Guide :material-open-in-new:](https://clm-community.gitlab-pages.dkrz.de/public/spice/add-ons/eva-suite.html){:target="_blank"}
- [Public repository on GitLab :material-open-in-new:](https://gitlab.dkrz.de/clm-community/public/evasuite){:target="_blank"}