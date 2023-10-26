---
title: COSMO
layout: default
nav_order: 1
parent: Models
---

# COSMO
The COSMO model is a limited-area, non-hydrostatic model developed by a collaboration of National Weather Services called the [Consortium for Small-scale Modeling](http://www.cosmo-model.org/).

C2SM currently facilitates the utilization of COSMO on the [Piz Daint](https://www.cscs.ch/computers/piz-daint) computing platform.

**Important note: C2SM's support for COSMO is scheduled to end in 2025**

## Access
In order to get access to the [COSMO repository](https://github.com/C2SM-RCM/cosmo) hosted on the C2SM-RCM GitHub organization,
please contact [C2SM Support](mailto:support@c2sm.ethz.ch).

Once you have access, clone the repository from GitHub using the SSH protocol:
```
git clone git@github.com:C2SM-RCM/cosmo.git
```
If you don't already have an SSH key set up for GitHub but would like to do so, follow the [instructions](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent).

## Configure and compile
For configuring and building COSMO with Spack, please refer to the official spack-c2sm documentation, which provides instructions for [setting up a Spack instance](https://c2sm.github.io/spack-c2sm/latest/QuickStart.html#at-cscs-daint-tsa-balfrin) and [installing COSMO](https://c2sm.github.io/spack-c2sm/latest/QuickStart.html#cosmo) on Piz Daint.

## Related tools
In the [Tools](https://c2sm.github.io/tools) section, you will find relevant tools for working with COSMO:
* [**Extpar:**](https://c2sm.github.io/tools/extpar.html) External parameters for the COSMO-grid (preprocessing)
* [**int2lm:**](https://c2sm.github.io/tools/int2lm.html) The interpolation software for the COSMO-model (preprocessing)
* [**Processing Chain**](https://c2sm.github.io/tools/processing_chain.html): Python workflow tool for COSMO


## Documentation
COSMO documentation is available at:
* [Official website of the Consortium for Small-scale Modeling (COSMO)](http://www.cosmo-model.org/)
* [COSMO Model System Overview](https://www.cosmo-model.org/content/model/cosmo/default.htm)
* [COSMO User's Guide](https://www.cosmo-model.org/content/model/cosmo/coreDocumentation/cosmo_userguide_6.00.pdf) 

## Asynchronous IO for NetCDF - A Guide for an optimal model setup

### Node configuration
When using asynchronous IO (Input/Output), the workload of the IO processors must be carefully balanced.
In general, no robust "rule of thumb" has been found, so some benchmark runs may be necessary.
Finding an optimal setup is not trivial, since the number of output namelists, the number of fields, and the number of IO processors may vary between different setups.
In particular, overloading the IO processors during model cleanup at the end of a job leads to additional runtime.
Note that using online compression can sometimes significantly increase the time and resources required for IO.

A quick overview of the actual workload on the IO processors can be obtained from the COSMO logs by increasing the verbosity settings of the log (`ldebug_io=.true.`, `idbg_level=6`):
```
Asyn-IO: block number xx was filled. Allocating a new block
```

The above log is printed each time a new buffer block is allocated.
This means that the Compute PEs (Processing Elements) store output data until the IO processors write it to disk.
If the number of allocated blocks increases during the simulation, i.e., more and more buffer blocks must be stored on the compute PEs after each output step, the IO processors won't write as fast as the model generates new output.

When the speed of writing data to disk by the IO processors and the model timestepping are in balance, the log message changes to:
```
 Asyn-IO: block number xx was filled, but the oldest one was released
```
It indicates that a balance has been reached between writing data to disk and the model generating new output.
In addition, each time an output file is completely written to disk, the corresponding IO processor prints a message that looks like this:

```
start_ionode:  Next asynchronous output will be done in step: xx
```

This log can give additional insight into how long it takes to write a file to disk.
In addition, there is a timer called `asyncio_wait` in the output section of YUTIMING. 

```
Output                         0.19         0.43         0.86        72.65
  computations O               0.08         0.11         0.16        17.71
  meta  data                   0.00         0.00         0.00         0.00
  write data                   0.00         0.19         0.55        32.70
  gather data                  0.10         0.12         0.14        20.35
  asynIO wait                  0.00         0.78         4.31       130.84
```
It provides information about how long all compute-PEs had to wait at the end of the simulation for all IO processors to finish writing data to disk.
This timer should be as small as possible.

### Zlib replacement for NetCDF compression
Online compression, enabled with the `lcompress_netcdf=.true.` parameter, uses the slower Zlib by default.
A speedup of a factor of two can be achieved by using Zlib_ng instead.
The `+zlib_ng` variant for building COSMO is required in combination with the command `spack load cosmo@master%pgi cosmo_target=gpu +zlib_ng` before execution.
Unfortunately, the convenient way of using RPATH for this feature is not possible.
