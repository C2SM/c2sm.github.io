
# DWD ICON Tools

The [DWD ICON Tools :material-open-in-new:](https://github.com/C2SM/icontools#dwd-icon-tools){:target="_blank"} contain a set of routines which may be suitable for reading, remapping and writing of fields from and to predefined grids,
e.g., regular (lat-lon, gaussian) or triangular (ICON). It can be used to generate lateral boundary conditions (LBC) and initial conditions (IC) for ICON-LAM simulations.

## Repository

In order to get access to the [DWD ICON Tools repository hosted on the C2SM GitHub organisation :material-open-in-new:](https://github.com/C2SM/icontools){:target="_blank"},
please contact your group's technical contact. They will be responsible for adding you to the appropriate user group.

## Web Interface

[Zonda](zonda.md) uses DWD ICON Tools under the hood: `icongridgen` is used to generate ICON grids, and `iconsub` is used to create the lateral boundary grid. Zonda is publicly available at [zonda.ethz.ch :material-open-in-new:](https://zonda.ethz.ch/){:target="_blank"}.

## Usage

### Säntis

On [Säntis](../hpc/santis.md), DWD ICON Tools is provided via the `climtools` uenv:

```
uenv start climtools/25.2:v1 --view=climtools
```

The resulting binaries (`iconremap`, `iconsub`, `icongridgen`, `icondelaunay`, `icongpi`) are directly available within this uenv.

### Euler

On [Euler](../hpc/euler.md), DWD ICON Tools can also be built directly against Euler's native module software stack.

Clone the repository with submodules:

```bash
git clone --recurse-submodules git@github.com:C2SM/icontools.git
cd icontools
```

Load the required modules: 

```bash
module load stack/2025-06 gcc/12.2.0 openmpi/4.1.7
module load netcdf-c/4.9.2 netcdf-fortran/4.6.1 hdf5/1.14.5 eccodes/2.34.0 libaec/1.0.6 libpng/1.6.39
```

Configure and build on a compute node:

```bash
srun -c 8 --time=00:15:00 bash -c './do_configure.sh && make -j 8'
```

The resulting binaries (`iconremap`, `iconsub`, `icongridgen`, `icondelaunay`, `icongpi`) are placed in the `icontools/` subdirectory.

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

    !!! note
    
        Ensure that `cdo` is available through uenv or has been installed.

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
