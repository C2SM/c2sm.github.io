# Derived Data Highlights

!!! info
    The datasets were created for quick multi-model ensemble assessments from monthly averaged fields. They include concatenated (historical + future scenario) members of the CMIP Next Generation archive in one file.   

!!! note
    Post-processing steps were performed by Anna Merrifield in the Climate Physics group. If any issues are found, please contact: [anna.merrifield@c2sm.ethz.ch](mailto:anna.merrifield@c2sm.ethz.ch).

### CMIPX-ng Stacked Files

<p align="center">
  <a href="images/C2SM_cmip5_gmst.png">
    <img src="images/C2SM_cmip5_gmst.png" width="300" alt="CMIP5">
  </a>
  <br>
  <em>Annual Average Global Mean Surface Temperature Anomaly with respect to 1871-1900 for CMIP5 multi-model ensembles of historical + (blue) RCP2.6, (yellow) RCP4.5, and (red) RCP8.5 projections.</em>
</p>

=== "IAC"
    ```console
    /net/atmos/data/...
    ```
- Size: 13GB
- Number of files: 16
- Access: direct / rsync
- Status: frozen (see below)

- Variable: tas
- Resolution: 2.5°x2.5°
- RCPs/SSPs: rcp26 (2025-09), rcp45 (2025-09), rcp85 (2023-09), SSP126 (), SSP245 (), SSP585 ()
- Time Aggregation: ann
- Coverage: global, western WCE region (-10. -- 15 degE, 45. -- 48. / 45. -- 54.65 degN)

- Variable: tas, pr
- Resolution: 2.5°x2.5°
- RCPs: rcp85 (2025-09)
- Time Aggregation: DJF, MAM, JJA, SON, ann
- Coverage: European domain (-10. -- 39. degE and 30. -- 76.25 degN)

- Ensemble Members: [CMIP5 Derived Member Lists](https://polybox.ethz.ch/index.php/s/cKxcLiG4w2Nq8P5)
