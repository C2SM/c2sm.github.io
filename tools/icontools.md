---
title: Icontools
layout: default
nav_order: 1
parent: Tools
---

## Icontools
Icontools contain a set of routines which may be suitable for reading, remapping and writing of fields from and to predefined grids,
e.g. regular (lat-lon, gaussian) or triangular (ICON). It can be used to genereta boundary and initial conditions for ICON-LAM simulations.

### Access
In order to get access to the [Icontools repository hosted on the C2SM GitHub organization](https://github.com/C2SM/icontools),
please contact your group's technical contact. They will be responsible for adding you to the appropriate user group.

## Compile
Spack takes care of configuring and building Iontools. For detailed instructions,
please consider the official spack-c2sm [documentation](https://c2sm.github.io/spack-c2sm/latests).
The following spack command should be sufficient for most cases:

```bash
spack install icontools@c2sm-master%gcc
```

## Run
The folder [C2SM in icontools](https://github.com/C2SM/icontools/tree/master/C2SM) contains a bunch of scripts to run iconremap and icongridgen on Piz Daint.
Most likely you will use the Icontools to generate a new grid or interpolate boundary conditions for limited-area Icon runs. 
Below is a recipe to create initial and boundary files for an ICON LAM run on Piz Daint. It is based on Bernhard's cases to create files based on ERA5 data.

### Generate new Icon grid

 ```bash
./icongridgen --nml gridgen.nml
``` 

### Interpolate BC from IFS
This manual refers to the workflow MeteoSwiss is currently using to run LAM-simulations.

* Add fields FI and z from IFS-analysis to BC prior the intepolation using CDO (GRIB-only).

```bash
cdo -selname,FI analysis fi_file
cdo -selname,z analysis z_file
cdo settime,'03:00:00'  fi_file fi_file_time
cdo settime,'03:00:00'  z_file z_file_time
cdo setreftime,2019-09-30,03:00:00  z_file_time z_file_reftime
cat file_for_BC zfile_reftime fi_file_time > complete_file
```

* Adapt scripts remap_ini and remap_lbc to your needs

* Remap IFS data for BC by

 ```bash
sbatch remap_lbc
``` 

* Remap IFS data for analysis

 ```bash
sbatch remap_ini
```

### Documentation
* A [Tex-version](https://github.com/C2SM/icontools/blob/master/doc/icontools_doc.tex) of the official documentation is in the repository.
* A [pdf-version](https://polybox.ethz.ch/index.php/s/P6zCBn5BIVzsxp7), 2020
