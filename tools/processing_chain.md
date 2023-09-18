---
title: Processing Chain
layout: default
parent: Tools
---

# COSMO/ICON Processing Chain

The Processing Chain is a collection of python scripts to prepare necessary input data, submit compute-jobs to the queue on Piz Daint and to apply post-processing steps. 
Besides being able to deal with standard versions of the COSMO or ICON model, it can als deal with several variants of them, namely COSMO-GHG, COSMO-ART and ICON-ART.
The chain can flexibly be adapted according to your needs, e.g., by creating your own case, adding new jobs or custom scripts.

The code is a product of a joint collaboration between Empa and C2SM. 
Originally, it has been developed by Chrstoph Knote using pure Bash scripts.
In 2018, Empa's [Atmospheric Modelling and Remote Sensing group](https://www.empa.ch/web/s503/modelling-remote-sensing) translated the code into Python,
making it more flexible and easier to maintain.

Since 2021, the Processing Chain is distributed to the whole C2SM
community and hosted at the C2SM GitHub organization.

has been adapted for running on Piz Daint and is distributed to users via the C2SM GitHub organization. Regular testing if performed via [Jenkins](https://jenkins-mch.cscs.ch/job/Spice/job/spice-weekly/) (requires access) to ensure that the code runs stably on the system.

If you need any help, please contact [Michael Jähn](https://c2sm.ethz.ch/the-center/people/person-detail.html?persid=286091).

## Code

* [Spice at the C2SM Github organization](https://github.com/C2SM/spice)
* [Spice at DKRZ GitLab (original code)](https://gitlab.dkrz.de/clm-community/spice) (requires access to DKRZ GitLab)

## Documentation

* [https://clm-docs.scrollhelp.site/spice-doc/](https://clm-docs.scrollhelp.site/spice-doc/)
