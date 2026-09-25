---
date:
  created: 2026-09-25
categories:
  - ICON
---

# ICON4Py dynamical core merged into ICON master

With this release, the GT4Py-based implementation of ICON's atmospheric dynamical core, developed within the EXCLAIM project at ETH Zürich, CSCS and MeteoSwiss, has been merged into the ICON master repository and is now available for general use. This is the first large component of ICON to be performance portable, and it marks the first concrete step towards a fully portable, architecture-agnostic ICON.

<!-- more -->

### What changed

The dynamical core- the part of ICON that solves the compressible, non-hydrostatic Navier–Stokes equations for wind, density, temperature and pressure, and which typically accounts for roughly 40% of the cost of an atmosphere-only run — has been rewritten using [GT4Py :material-open-in-new:](https://gridtools.github.io/gt4py/){:target="_blank"}, a Python-embedded domain-specific language for weather and climate codes developed at ETH Zürich. The Fortran+OpenACC version remains fully supported; the new component, referred to as **ICON4Py**, can be enabled as an alternative dynamical core via a build flag and is invoked directly from the existing Fortran driver through a lightweight interface layer (`py2fgen`), so no changes are required to the rest of a user's model setup.

<!-- TODO: add link to build instructions here -->

Rather than hand-tuning OpenMP/OpenACC directives for each target machine, ICON4Py expresses the numerics once, as field and scan operators over the unstructured ICON grid, and let the GT4Py backend generate optimized code for the target hardware. Currently NVIDIA, AMD GPUs, and x86/ARM CPUs are supported. The same Python source is compiled differently depending on the machine it runs on, rather than being interleaved with machine-specific pragmas. Halo exchanges are handled by the GHEX library, which supports multiple communication back ends (MPI, UCX, NCCL) without changes to the user code.

### Why this matters

ICON's Fortran+OpenACC implementation has been extensively performance-tuned over the years, but that tuning is tied to specific compilers and architectures and is increasingly costly to maintain as compiler support for Fortran on new HPC platforms lags behind C++ and Python toolchains. ICON4Py decouples the numerical description from the target architecture, so that porting to new hardware becomes a backend change rather than a rewrite of the science code, and it opens the door to closer integration with the wider Python/ML ecosystem (NumPy, CuPy, JAX) for future hybrid and machine-learning-augmented components.

### Performance

ICON4Py's dynamical core integrated with the rest of Fortran+OpenACC code has demonstrated improved performance despite the overhead of the Python interface. In production-grade coupled atmosphere–land and atmosphere–land–ocean configurations on CSCS's ALPS infrastructure, its dynamical core runs **20–30% faster** than the reference Fortran+OpenACC implementation. This translates into an **~10–15% speed-up of the full coupled simulation** (Dipankar et al., 2026; Bianco et al., 2026). At R2B10 (2.5 km global grid spacing, 120 atmosphere and 72 ocean vertical levels), the new software reaches a throughput of **160 simulated days per day (SDPD)** at 3200 GPUs.

Reliability of the refactored code is tested regularly with a three-tier strategy: correctness checks on segments of the dynamical core (including diffusion) that span between halo exchanges, against relative-error tolerances of 10⁻¹² (softened to 10⁻⁷ where floating-point reordering requires it); live comparison of the full dynamical core running inside the Fortran host code against the Fortran+OpenACC reference on identical inputs; and a numerical error-growth check ("probtest") over 5–10 ICON time steps against a perturbed reference ensemble.

### Scientific results

The new software has already been used for several published storm-resolving global simulations:

- Global aquaplanet runs at 2.5 km, 20 km and 80 km grid spacing, using a jet-streak tracking method to show that convection-permitting resolution produces a stronger, poleward-shifted eddy-driven jet with a clear separation from the subtropical jet (Bukenberger et al., 2026);
- Global uncoupled runs with idealized SST perturbations, used to study how convection- and gravity-wave-parameterization choices affect the tropical ITCZ at 5 km vs. 40 km resolution (Kroll et al., 2025, *Atmos. Chem. Phys.*);
- A four-year global uncoupled simulation at 2.5 km with realistic prescribed SSTs, contributing to the DYAMOND phase-III protocol, which eliminates the long-standing "double ITCZ" bias seen in coarser ICON-Sapphire configurations and captures the major global monsoon systems in broad agreement with GPM IMERG observations (Prein et al., 2026, *Geosci. Model Dev.*);
- A systematic grid-spacing sensitivity study (80/40/10 km) of Northern Hemisphere monsoons, showing that ICON captures the global monsoon domain and regional onset with good skill, while finding that finer grid spacing does not uniformly improve monsoon simulation — it sharpens the diurnal cycle but amplifies mean and variability biases over South Asia and West Africa (Pothapakula et al., 2026, *Weather Clim. Dynam.*);
- A multiscale evaluation of Indian monsoon rainfall against five CMIP6-class models at ~40 km resolution, finding ICON's non-hydrostatic dynamical core gives it an edge in diurnal timing and phase representation relative to hydrostatic CMIP6 models, at the cost of some amplitude biases over the Bay of Bengal (Pokhrel et al., 2026, *Weather Clim. Dynam.*).

### What's next

The current merge covers a significant milestone of the EXCLAIM roadmap: performance portable dynamical core embedded in the existing Fortran+OpenACC driver targeted at global km-scale simulations. Work is already under way on a fully portable Python-based ICON atmospheric module with GT4Py/Kokkos physics components. These will be reported as they reach maturity.

### References

- Dipankar, A. et al., 2026: Toward exascale climate modelling: a python DSL approach to ICON's (icosahedral non-hydrostatic) dynamical core (icon-exclaim v0.2.0). *Geosci. Model Dev.*, 19, 713–729. [https://doi.org/10.5194/gmd-19-713-2026 :material-open-in-new:](https://doi.org/10.5194/gmd-19-713-2026){:target="_blank"}
- Bianco, M. et al., 2026: Integrating a Python Dynamical core into ICON. *arXiv:2608.21150*.
- Bukenberger, M., Schemm, S., Dipankar, A. et al., 2026: Resolution-dependent jet stream representation in ICON aquaplanet experiments. *ESS Open Archive* \[preprint\]. [https://doi.org/10.22541/essoar.15006621/v1 :material-open-in-new:](https://doi.org/10.22541/essoar.15006621/v1){:target="_blank"}
- Prein, A. F., Pothapakula, P. K., Zeman, C., Lalonde, M., Rixen, M., Dipankar, A., Leclair, M., and Jocksch, A., 2026: From single storms to large-scale waves: a multi-year kilometer-scale global simulation. *Geosci. Model Dev.*, 19, 5277–5303. [https://doi.org/10.5194/gmd-19-5277-2026 :material-open-in-new:](https://doi.org/10.5194/gmd-19-5277-2026){:target="_blank"}
- Kroll, C. A. et al., 2025: Parameterization adaptation needed to unlock the benefits of increased resolution for the ITCZ in ICON. *Atmos. Chem. Phys.*, 25, 16915–16943.
- Pothapakula, P. K., Prein, A. F., Sunkisala, A., and Dipankar, A., 2026: Global monsoon in ICON: the scale-dependent response of Northern Hemisphere monsoons. *Weather Clim. Dynam.*, 7, 979–1007. [https://doi.org/10.5194/wcd-7-979-2026 :material-open-in-new:](https://doi.org/10.5194/wcd-7-979-2026){:target="_blank"}
- Pokhrel, S. et al., 2026: Multiscale assessment of Indian monsoon rainfall using ICON and CMIP6 model simulations. *Weather Clim. Dynam.*, 7, 1447–1477. [https://doi.org/10.5194/wcd-7-1447-2026 :material-open-in-new:](https://doi.org/10.5194/wcd-7-1447-2026){:target="_blank"}
- Code: ICON4Py, [https://github.com/C2SM/icon4py :material-open-in-new:](https://github.com/C2SM/icon4py){:target="_blank"}
