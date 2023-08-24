---
title: Int2lm
layout: default
nav_order: 1
parent: Tools
---

## Int2lm
Int2lm is an interpolation program providing boundary and/or initial conditions to the Cosmo model.

### Access
In order to get access to the [Int2lm repository hosted on the C2SM-RCM GitHub organization](https://github.com/C2SM-RCM/int2lm), 
please contact support@c2sm.ethz.ch.

### Compile
## Compile
Spack takes care of configuring and building int2lm. For detailed instructions,
please consider the official spack-c2sm [documentation](https://c2sm.github.io/spack-c2sm/latest).


### Additional features for C2SM version
There are features that could not be merged into the COSMO-ORG version before the end of development.
Therefore a separate [branch c2sm-features](https://github.com/C2SM-RCM/int2lm/tree/c2sm-features) has been created.

#### Read only subset of coarse netcdf input data 
dd new namelist entries for passing start indices of NetCDF input. 
Doing so mitigates slow down for large input-files via new namelist parameters in namelist `&GRID_IN`:

* ie_in_start_io (start index in i-direction)
* je_in_start_io (start index in k-direction) 

The parameters ie_in_tot and je_in_tot define the length of the data to be read, instead of the total lenght present in the NetCDF input file. 

**Schematic about the two ways for reading NetCDF input files**
