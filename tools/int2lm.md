---
title: INT2LM
layout: default
parent: Tools
---

# INT2LM

INT2LM is an interpolation program providing boundary and/or initial conditions to the COSMO model.

## Support status

## Access

In order to get access to the [INT2LM repository hosted on the C2SM-RCM GitHub organization](https://github.com/C2SM-RCM/int2lm), 
please contact [C2SM Support](mailto:support@c2sm.ethz.ch).

## Compile

Spack takes care of configuring and building INT2LM. For detailed instructions,
please consider the official [spack-c2sm documentation](https://c2sm.github.io/spack-c2sm/latest).

## Additional features for C2SM version

There are features that could not be merged into the COSMO-ORG version before the end of development.
Therefore a separate [branch c2sm-features](https://github.com/C2SM-RCM/int2lm/tree/c2sm-features) was created.

### Read only subset of coarse netcdf input data 

Add new namelist entries for passing start indices of NetCDF input. 
This mitigates slowdown for large input files via new namelist parameters in namelist `&GRID_IN`:

* `ie_in_start_io` (start index in `i`-direction)
* `je_in_start_io` (start index in `k`-direction) 

The parameters `ie_in_tot` and `je_in_tot` define the length of the data to be read, instead of the total length present in the NetCDF input file. 

### Schematic about the two ways for reading NetCDF input files
![](images/int2lm_subset_schematic.png)
