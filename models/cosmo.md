---
title: COSMO
layout: default
nav_order: 1
parent: Models
---

## COSMO: A non-hydrostatic limited-area atmospheric weather and climate model 
The COSMO model is a limited area, non-hydrostatic model developed by a collaboration of National Weather Services called the [COSMO Consortium](http://www.cosmo-model.org/).

### Access
In order to get access to the [COSMO repository hosted on the C2SM-RCM GitHub organization](https://github.com/C2SM-RCM/cosmo),
please contact support@c2sm.ethz.ch.

### Compile
Spack takes care of configuring and building COSMO. For detailed instructions, 
please consider the official spack-c2sm [documentation](https://c2sm.github.io/spack-c2sm/v0.18.1.11/QuickStart.html#cosmo).

### Toolset
* [**Extpar:**](https://c2sm.github.io/tools/extpar.html) External parameters for the COSMO-grid (preprocessing)
* [**int2lm:**](https://c2sm.github.io/tools/int2lm.html) The interpolation software for the COSMO-model (preprocessing)


### Documentation
* [Official website of the Consortium for Small-scale Modeling (COSMO)](http://www.cosmo-model.org/)
* [COSMO Model System Overview](http://cosmo-model.org/content/model/default.htm)
* [COSMO User's Guide](http://cosmo-model.org/content/model/documentation/core/cosmo_userguide_5.04.pdf) 

### Asynchronous IO for NetCDF - A Guide for an optimal model setup

#### Node configuration
When using asynchronous IO, the workload of the IO-processors needs to be balanced carefully. In general, no robust "rule of thumb" has been found, 
and thus a few benchmark runs may be needed. An optimal setup is not trivial to find because the number of output-namelists, the number of fields 
and the number of IO-processors may change between different setups. In particular, overload on the IO-processors leads to additional runtime during 
model cleanup at the end of a job. Since the compute nodes are not released from the job, all of them will idle while 
the remainder of the output is processed. note that employing online compression can sometimes add substantially to the time and resources needed for IO

A brief overview on the actual workload on the IO-processors can be gained from the COSMO logs, when increasing the the verbosity-settings of the log (ldebug_io=.true., idbg_level=6):
```
Asyn-IO: block number xx was filled. Allocating a new block
```

The log above is printed every time a new buffer block is allocated. This means, that the compute PE's store output 
data until the IO-processors wrote it to disk. In case the number of blocks allocated increases throughout the simulation, 
i.e. after every output step more and more buffer blocks need to be stored on the compute PE's, 
the IO-processors don’t write as fast as the model generates new output.

In case the speed of writing data to disk by the IO-processors and the model timestepping is in equilibrium the log message changes to: 

```
 Asyn-IO: block number xx was filled, but the oldest one was released
```
It indicates, that an equilibrium between writing data to disk and the model
generating new output has been established.
Additionally every time an output file has been completetely written to disk, 
the corresponding IO-processor prints out a message as follows: 

```
start_ionode:  Next asynchronous output will be done in step: xx
```

This log may give additional insight about how long it takes to write a file to disk.
Additionally, in YUTIMING there is a timer called asyncio_wait in the Output section. 

```
Output                         0.19         0.43         0.86        72.65
  computations O               0.08         0.11         0.16        17.71
  meta  data                   0.00         0.00         0.00         0.00
  write data                   0.00         0.19         0.55        32.70
  gather data                  0.10         0.12         0.14        20.35
  asynIO wait                  0.00         0.78         4.31       130.84
```
It provides information about how long all compute-PE needed to wait at the end of the simulation for all IO-processors to finish writing data to disk. This timer should be as small as possible.

### Zlib replacement for NetCDF compression
The online compression, activated with parameter `lcompress_netcdf=.true.`, 
uses by default the not so fast Zlib. A speedup of a factor two can be obeserved in case Zlib_ng is used instead. 
The variant `+zlib_ng` for building COSMO in combination with the command 
`spack load cosmo@master%pgi cosmo_target=gpu +zlib_ng`
prior to run is neccesary. Unfortunately the convenient way of using RPATH for that feature is not possible.