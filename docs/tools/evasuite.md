# EvaSuite

EvaSuite is an addon for SPICE but also a standalone software for either

1. Compare your simulation experiment with E-OBS or ERA5.
2. Compare your simulation experiment and a reference simulation with E-OBS or ERA5.

## Instructions to Set Up on Säntis

### Setup Miniforge

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

### Installation

Follow `DOCS/installation.md`:

1. **Clone the repository**
```bash
git clone --recurse-submodules git@gitlab.dkrz.de:clm-community/evasuite/HZG_Evaluation_Suite.git EvaSuite_v1.0
```

If you don't have access to the EvaSuite repository, you can download the code from Zenodo:

!!! todo
    Zenodo link.



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


## Usage

Load modules and activate environment:
```bash
uenv start --view=modules netcdf-tools/2024:v1
module load cdo/2.4.0 netcdf-c/4.9.2 netcdf-fortran/4.6.1
conda activate py310_evasuite
```

## Reference

- [Documentation :material-open-in-new:](https://hereon-coast.atlassian.net/wiki/spaces/SPICE/pages/983091/eva-Suite){:target="_blank"}
- [Repository on GitLab :material-open-in-new:](https://gitlab.dkrz.de/clm-community/evasuite/HZG_Evaluation_Suite){:target="_blank"} (need DKRZ account and access rights)