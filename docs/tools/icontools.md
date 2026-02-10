
# DWD ICON Tools

The [DWD ICON Tools :material-open-in-new:](https://github.com/C2SM/icontools#dwd-icon-tools){:target="_blank"} contain a set of routines which may be suitable for reading, remapping and writing of fields from and to predefined grids,
e.g., regular (lat-lon, gaussian) or triangular (ICON). It can be used to generate lateral boundary conditions (LBC) and initial conditions (IC) for ICON-LAM simulations.

## Support status

The `master` branch of the [DWD ICON Tools :material-open-in-new:](https://github.com/C2SM/icontools){:target="_blank"} is integrated in the [`spack-c2sm` system tests :material-open-in-new:](https://github.com/C2SM/spack-c2sm/blob/main/test/common_system_test.py){:target="_blank"} on Balfrin.

## Repository

In order to get access to the [DWD ICON Tools repository hosted on the C2SM GitHub organisation :material-open-in-new:](https://github.com/C2SM/icontools){:target="_blank"},
please contact your group's technical contact. They will be responsible for adding you to the appropriate user group.

## Usage

### 1) Shipped via uenv

On [Säntis](../hpc/santis.md), DWD ICON Tools is provided via the `climtools` uenv:

```
uenv start climtools/25.2:v1 --view=climtools
```

### 2) Compile manually via Spack

[Spack](spack.md) takes care of configuring and building DWD ICON Tools. For detailed instructions,
please consider the official [spack-c2sm documentation :material-open-in-new:](https://c2sm.github.io/spack-c2sm/latest){:target="_blank"}.
The following Spack installation should be sufficient for most cases.

Clone the C2SM Spack main branch and source it:
```bash
git clone --depth 1 --recurse-submodules --shallow-submodules https://github.com/C2SM/spack-c2sm.git
source ./spack-c2sm/setup-env.sh /user-environment
```

Install the ICON Tools:
```bash
spack install icontools@c2sm-master%gcc
```

!!! note
    If all dependencies have to be installed from scratch, this may take a while.

After the installation, you need to load the package with Spack:

```bash
spack load icontools
```

## Run

[The folder C2SM in the icontools repository :material-open-in-new:](https://github.com/C2SM/icontools/tree/master/C2SM){:target="_blank"} contains a bunch of scripts to run `iconremap` and `icongridgen` on Säntis.
Most likely you will use the DWD ICON tools to generate a new grid or interpolate boundary conditions for limited-area ICON runs. 

Below is a recipe to create initial and boundary files for an ICON-LAM run on Säntis.

### Clone the repository

```bash
git clone git@github.com:C2SM/icontools.git
```

### Generate a new ICON grid

```bash
icongridgen --nml icontools/C2SM/gridgen.nml
``` 

### Interpolate BC from IFS

This manual refers to the workflow MeteoSwiss currently uses to run LAM simulations.

* Add fields `FI` and `z` from IFS analysis to LBC prior to the interpolation using `cdo` (GRIB only). 
To use the `cdo` command, make sure that a proper user environment is loaded containing `cdo`.

    ```bash
    cdo -selname,FI analysis_file fi_file
    cdo -selname,z analysis_file z_file
    cdo settime,'03:00:00' fi_file fi_file_time
    cdo settime,'03:00:00' z_file z_file_time
    cdo setreftime,2019-09-30,03:00:00  z_file_time z_file_reftime
    cat lbc_file zfile_reftime fi_file_time > complete_file
    ```

* Adapt scripts `icontools/C2SM/remap_ini` and `icontools/C2SM/remap_lbc` to your needs

* Remap IFS data for BC:

    ```bash
    sbatch -A <account> icontools/C2SM/remap_lbc
    ``` 

* Remap IFS data for analysis:

    ```bash
    sbatch -A <account> icontools/C2SM/remap_ini
    ```

## Documentation

* A [TeX version :material-open-in-new:](https://github.com/C2SM/icontools/blob/master/doc/icontools_doc.tex){:target="_blank"} of the official documentation is in the repository
* A [pdf version :material-open-in-new:](https://polybox.ethz.ch/index.php/s/jdYaNrWFF8LjcrF){:target="_blank"}, Oct 2025
