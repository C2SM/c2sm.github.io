# Compiling `icon-nwp` on Santis with GPU Support and ComIn Integration

This guide provides a step-by-step recipe to compile **`icon-nwp`** on **Santis** with GPU support and enable **ComIn** functionality.  
It includes environment setup, code compilation, and configuration steps for running ICON with the ComIn plugin.

!!! note "Important Notes"

    - The **`master`** branch of [`icon-nwp` :material-open-in-new:](https://gitlab.dkrz.de/icon/icon-nwp){:target="_blank"} does **not** currently include the latest ComIn updates.  
    A manual fix is required to make ComIn work on GPUs, following this commit:  
    [ComIn Commit f9e1c2f :material-open-in-new:](https://gitlab.dkrz.de/icon-comin/comin/-/commit/f9e1c2fe9e17650e55ccf82f5e1b8e872fc658c7){:target="_blank"}

    - Further ComIn bug fixes are under development. Updates will be merged into `icon-nwp` when available.

    - Replace all instances of `<username>` with your actual username.

## 1. Pull and Start the ICON Environment

```bash
uenv image pull icon/25.2:v1
uenv start icon/25.2:v1 --view modules
```

## 2. Install a Custom Spack Instance

```bash
git clone --depth 1 --recurse-submodules --shallow-submodules -b v0.22.2.2 \
    https://github.com/C2SM/spack-c2sm.git $SCRATCH/spack-c2sm-nwp
```

Load the Spack instance:

```bash
source $SCRATCH/spack-c2sm-nwp/setup-env.sh /user-environment
```

## 3. Clone and Prepare the ICON Code

```bash
git clone git@gitlab.dkrz.de:icon/icon-nwp.git ./icon-nwp
cd ./icon-nwp
git submodule update --init --recursive
```

## 4. Set Up the Build Directory

```bash
mkdir gpu && cd gpu
mkdir santis && touch ./santis/spack.yaml
```

Copy the contents of the `spack.yaml` file below into `./santis/spack.yaml`.

<details>

<summary>spack.yaml</summary>

```yaml
# ICON
#
# ------------------------------------------
# Copyright (C) 2004-2025, DWD, MPI-M, DKRZ, KIT, ETH, MeteoSwiss
# Contact information: icon-model.org
# See AUTHORS.TXT for a list of authors
# See LICENSES/ for license information
# SPDX-License-Identifier: BSD-3-Clause
# ------------------------------------------

spack:
  specs:
  - py-numpy
  - py-scipy
  - py-xarray
  - py-mpi4py
  - py-netcdf4
  - py-scikit-learn
  - py-shapely
  - cosmo-eccodes-definitions@2.36.0.3
  - icon @develop %nvhpc +comin +grib2 +eccodes-definitions +ecrad +emvorado +art +dace gpu=nvidia-90
    +mpi-gpu +realloc-buf ~aes ~jsbach ~ocean ~coupling ~rte-rrtmgp ~loop-exchange
    ~async-io-rma ~cuda-graphs fflags="-traceback"
  view: true
  concretizer:
    unify: true
  packages:
    icon:
      package_attributes:
        build_directory: gpu
  develop:
    icon:
      spec: icon @develop %nvhpc +comin +grib2 +eccodes-definitions +ecrad +emvorado +art +dace gpu=nvidia-90 +mpi-gpu +realloc-buf ~aes ~jsbach ~ocean ~coupling ~rte-rrtmgp ~loop-exchange ~async-io-rma ~cuda-graphs fflags="-traceback" 
      path: /capstor/scratch/cscs/<username>/icon-nwp
```

</details>

## 5. Activate the Spack Environment and Build ICON

```bash
spack env activate -p -d santis/
spack concretize -f
spack install -v
```

## 6. Create a Python Virtual Environment for ComIn

```bash
python -m venv venv-comin
source ./venv-comin/bin/activate
```

Install required Python packages:

```bash
pip install --upgrade pip
pip install cupy numpy scipy xarray mpi4py netcdf4 shapely scikit-learn pyyaml
```

## 7. Build ComIn

Enter the Spack build environment and compile ComIn:

```bash
spack build-env icon -- bash
cd ./externals/comin/build
cmake -DCOMIN_ENABLE_EXAMPLES=ON -DCOMIN_ENABLE_PYTHON_ADAPTER=ON .
make
```

## 8. Add ComIn to the ICON Namelist

In your ICON namelist, include the following section:

```fortran
&comin_nml
  plugin_list(1)%name           = "comin_plugin"
  plugin_list(1)%plugin_library = "/capstor/scratch/cscs/<username>/icon-nwp/gpu/externals/comin/build/plugins/python_adapter/libpython_adapter.so"
  plugin_list(1)%options        = "<comin_python_script_path>"
/
```

## 9. Configure the Slurm Job

In your Slurm job script, load the Spack environment and activate the Python virtual environment:

```bash
# Load Spack environment
source $SCRATCH/spack-c2sm-nwp/setup-env.sh /user-environment
spack env activate -p -d /capstor/scratch/cscs/<username>/icon-nwp/gpu/santis/

# Set Python executable for ComIn
export COMIN_PYTHON_EXECUTABLE="/capstor/scratch/cscs/<username>/icon-nwp/gpu/venv-comin/bin/python"

# Load necessary modules
module load cray-mpich

echo "Environment loaded"
```