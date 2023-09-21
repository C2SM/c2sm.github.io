---
title: CORDEX-FPSCONV data
layout: default
nav_order: 1
parent: datasets
---

# CORDEX-FPSCONV data

The CORDEX-FPSCONV dataset is a multi-model ensemble of convection permitting regional climate model runs created within [WCRP-CORDEX](https://cordex.org/experiment-guidelines/flagship-pilot-studies/endorsed-cordex-flagship-pilote-studies/europe-mediterranean-convective-phenomena-at-high-resolution-over-europe-and-the-mediterranean/).
The model runs are described in [Coppola et al. 2020](https://link.springer.com/article/10.1007/s00382-018-4521-8), [Ban et al. 2021](https://link.springer.com/article/10.1007/s00382-021-05708-w) and [Pichelli et al. 2021](https://link.springer.com/article/10.1007/s00382-021-05657-4) and cover the ALP-3 domain.
![](images/ALP-3-crop.png)

So far, only the data from ETH (CLMcom-ETH-COSMO-crCLIM) has been CMORized, for all other models the data format is a preliminary version (from ~September 2022) and not the one that will go to ESGF.
At the moment, the data archive at CSCS (/store/c2sm/c2sme/CH202X/CORDEX-FPSCONV/) contains mainly 1-hourly precipitation and temperature and daily maximum temperature and minimum temperature.
These 4 variables have been used in three MSc theses and went through basic checks. The other variables (in 6hr, day) have been copied from the Jülich server but have not been used and were not checked.

Four different time periods are available:
* Evaluation: ca. 2000-2009 (varies for some models)
* Historical: ca. 1996-2005 (varies for some models)
* RCP8.5: 2041-2050 and 2090-2099 (not all modelling groups run both time periods) 

Every modelling group run an evaluation run (precipitation is described in Ban et al. 2021).
Not all groups continued to run historical and rcp8.5 runs.
The groups running WRF joined together to run historical and scenario runs (therefore they were sometimes run on different machines).

An overview over which variables are available for which runs can be found [here](https://www.polybox.ethz.ch/index.php/s/hVYniBtoaneP9Lc).
More details on the different model runs e.g. info about the driving RCM and domains is [here](https://docs.google.com/spreadsheets/d/1wrt8Rcquk7dgIumGJeEc06irpkBwZtq_b7Pn3UhiT2g/edit?usp=sharing).
