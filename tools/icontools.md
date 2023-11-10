---
title: DWD ICON Tools
layout: default
parent: Tools
---

# DWD ICON Tools

The DWD ICON Tools contain a set of routines which may be suitable for reading, remapping and writing of fields from and to predefined grids,
e.g. regular (lat-lon, gaussian) or triangular (ICON). It can be used to generate lateral boundary conditions (LBC) and initial conditions (IC) for ICON-LAM simulations.

## Support status

## Access

In order to get access to the [DWD ICON Tools repository hosted on the C2SM GitHub organization](https://github.com/C2SM/icontools),
please contact your group's technical contact. They will be responsible for adding you to the appropriate user group.

## Compile

Spack takes care of configuring and building Icontools. For detailed instructions,
please consider the official [spack-c2sm documentation](https://c2sm.github.io/spack-c2sm/latest).
The following Spack installation should be sufficient for most cases:

```bash
spack install icontools@c2sm-master%gcc
```

After the installation, you need to load the package with Spack:

```bash
spack load icontools
```

## Run

[The folder C2SM in the icontools repository](https://github.com/C2SM/icontools/tree/master/C2SM) contains a bunch of scripts to run `iconremap` and `icongridgen` on Piz Daint.
Most likely you will use the DWD ICON tools to generate a new grid or interpolate boundary conditions for limited-area ICON runs. 

Below is a recipe to create initial and boundary files for an ICON-LAM run on Piz Daint.

### Clone the repository
```bash
git clone git@github.com:C2SM/icontools.git
```

### Generate a new ICON grid

 ```bash
icongridgen --nml icontools/C2SM/gridgen.nml
``` 

### Interpolate BC from IFS

This manual refers to the workflow MeteoSwiss is currently using to run LAM simulations.

* Add fields `FI` and `z` from IFS analysis to LBC prior to the interpolation using `cdo` (GRIB only). To use the `cdo` command, make sure the module is loaded: `module load daint-gpu CDO`.

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

* A [TeX version](https://github.com/C2SM/icontools/blob/master/doc/icontools_doc.tex) of the official documentation is in the repository
* A [pdf version](https://polybox.ethz.ch/index.php/s/jdYaNrWFF8LjcrF), Sept 2023
