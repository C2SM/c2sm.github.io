
# Tools

C2SM supports a set of pre- and postprocessing tools on different high-performance platforms.

## Pre-processing

<div class="grid cards" markdown>

-   :material-map-legend:{ .lg .middle } **DWD ICON Tools**

    ---

    Routines for reading, remapping and writing fields on ICON grids; generate lateral boundary and initial conditions for ICON-LAM simulations.

    [:octicons-arrow-right-24: DWD ICON Tools](icontools.md)

-   :material-earth:{ .lg .middle } **EXTPAR**

    ---

    Prepares external parameter data files used as input for the ICON model.

    [:octicons-arrow-right-24: EXTPAR](extpar.md)

</div>

## Workflow Tools

<div class="grid cards" markdown>

-   :material-chili-hot:{ .lg .middle } **SPICE**

    ---

    Starter Package for ICON-CLM Experiments — handles pre-processing, namelist setup, simulation and archiving.

    [:octicons-arrow-right-24: SPICE](spice.md)

-   :material-pipe:{ .lg .middle } **Processing Chain**

    ---

    Python workflow tool for preparing input data, submitting SLURM jobs, and post-processing COSMO and ICON model setups.

    [:octicons-arrow-right-24: Processing Chain](processing_chain.md)

</div>

## HPC Utilities

<div class="grid cards" markdown>

-   :material-package-variant:{ .lg .middle } **Spack-C2SM**

    ---

    C2SM's configuration of the Spack package manager for installing ICON and related software on HPC systems.

    [:octicons-arrow-right-24: Spack-C2SM](spack.md)

-   :material-chart-bar:{ .lg .middle } **Scaling Analysis**

    ---

    Automates creation of multiple ICON run scripts with varying node counts to assess strong scaling performance.

    [:octicons-arrow-right-24: Scaling Analysis](scaling_analysis.md)

</div>

## Web Tools

<div class="grid cards" markdown>

-   :material-weather-windy:{ .lg .middle } **Zephyr**

    ---

    Climate data extraction tool and web interface for requesting climate model and reanalysis datasets managed by C2SM.

    [:octicons-arrow-right-24: Zephyr](zephyr.md)

-   :material-dice-d20:{ .lg .middle } **Zonda**

    ---

    Web interface for generating EXTPAR data on ICON triangular grids for research and on-demand simulations.

    [:octicons-arrow-right-24: Zonda](zonda.md)

</div>
