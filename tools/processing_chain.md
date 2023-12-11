---
title: Processing Chain
layout: default
parent: Tools
---

# Processing Chain <img src="https://polybox.ethz.ch/index.php/s/yc3zMmoXKyI2rJm/download" width="64" valign="middle"/> 

The Processing Chain is a collection of Python scripts to prepare the necessary input data, submit the compute jobs to the queue on Piz Daint and to apply post-processing steps. 
In addition to the standard versions of the COSMO and ICON models, it can als handle several variants of these models, namely COSMO-GHG, COSMO-ART and ICON-ART.
The chain can be flexibly adapted according to your needs, e.g., by creating your own case, adding new jobs or custom scripts.

The code is the product of a joint collaboration between Empa and C2SM. 
It was originally developed by Christoph Knote using pure Bash scripts.
In 2018, Empa's [Atmospheric Modelling and Remote Sensing group](https://www.empa.ch/web/s503/modelling-remote-sensing) translated the code into Python,
making it more flexible and easier to maintain.

Since 2021, the Processing Chain has been distributed to the entire C2SM
community and hosted on the [C2SM GitHub organization](https://github.com/C2SM/processing-chain/). Regular testing is done via [Jenkins](https://jenkins-mch.cscs.ch/job/ProcessingChain/job/processing-chain-weekly/) (requires access) to ensure that the code runs stably on the system.

If you need any help, please contact [Michael Jähn](https://c2sm.ethz.ch/the-center/people/person-detail.html?persid=286091).

## Support status

The `main` branch is continuously tested on Piz Daint.

## Features

- Automatic folder structure creation
- Easy creation of own cases
- Namelist templates
- Nested runs possible
- Different examples for COSMO and ICON available
- and much more!

## Code and Documentation

* [Processing Chain at the C2SM Github organization](https://github.com/C2SM/processing-chain)

