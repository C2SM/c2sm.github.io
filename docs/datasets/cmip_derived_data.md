# CMIP Derived Data

## CMIP Next Generation

!!! info
    The datasets are checked, standardized, and regridded to common grid.

!!! note
    Next Generation (ng) archives were maintained by Reto's group (Jan Sedlacek/Lukas Brunner). Ruth Lorenz / C2SM took over cmip6-ng in 2022. Contact: [cmip6-archive@env.ethz.ch](mailto:cmip6-archive@env.ethz.ch). Documentation: [https://doi.org/10.5281/zenodo.373412 :material-open-in-new:](https://doi.org/10.5281/zenodo.3734128){:target="_blank"}.

### CMIP3-ng

=== "IAC"
    ```console
    /net/atmos/data/cmip3-ng
    ```

- Size: 0.5 TB
- Number of files: 5.000
- Access: direct / rsync
- Status: frozen (2019-03)
- Variables: n/a
- Resolution: native and 2.5°x2.5°
- Coverage: global

### CMIP5-ng

=== "IAC"
    ```console
    /net/atmos/data/cmip5-ng
    ```

- Size: 33 TB
- Number of files: 100.000
- Access: direct / rsync
- Status: frozen (2019-03)
- Variables: n/a
- Resolution: native and 2.5° x 2.5°
- Coverage: global

### CMIP6-ng

=== "IAC"
    ```console
    /net/atmos/data/cmip6-ng
    ```
=== "Euler"
    ```console
    /nfs/atmos/c2sm/cmip6-ng
    ```

- Size: 216.74 TB :material-information-outline:{ title="last updated: 2026-05-31 01:46:54" }
- Number of files: 725,518 :material-information-outline:{ title="last updated: 2026-05-31 01:46:54" }
- Access: direct / rsync
- Status: updated monthly
- Variables:
  `areacella`{ title="fx (native)" },
  `clt`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `co2mass`{ title="mon (native)" },
  `evspsbl`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `evspsblsoi`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `evspsblveg`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `gpp`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `hfds`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `hfls`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `hfss`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `hurs`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `huss`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `lai`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `masks`{ title="fx (native)" },
  `mlotst`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `mrro`{ title="ann (g025), ann (native), day (g025), day (native), mon (g025), mon (native)" },
  `mrros`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `mrso`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `mrsol`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `mrsos`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `nbp`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `npp`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `pr`{ title="ann (g025), ann (native), day (g025), day (native), mon (g025), mon (native)" },
  `prw`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `ps`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `psl`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `ra`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `rh`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `rlds`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `rldscs`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `rlus`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `rlut`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `rlutcs`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `rsds`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `rsdscs`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `rsdt`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `rsus`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `rsuscs`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `rsut`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `rsutcs`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `rtmt`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `sfcWind`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `sftlf`{ title="fx (native)" },
  `siconc`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `sos`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `ta`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `tas`{ title="ann (g025), ann (native), day (g025), day (native), mon (g025), mon (native)" },
  `tasmax`{ title="ann (g025), ann (native), day (g025), day (native), mon (g025), mon (native)" },
  `tasmin`{ title="ann (g025), ann (native), day (g025), day (native), mon (g025), mon (native)" },
  `tauu`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `tauv`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `tos`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `tran`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `treeFrac`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `tsl`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `uas`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `vas`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `zg500`{ title="ann (g025), ann (native), day (g025), day (native), mon (g025), mon (native)" },
  `zos`{ title="ann (g025), ann (native), mon (g025), mon (native)" }
- Resolution: native and 2.5° x 2.5°
- Coverage: global
- Link to [CMIP6KnownIssues :material-open-in-new:](https://wiki.iac.ethz.ch/Climphys/CMIP6KnownIssues){:target="_blank"}
