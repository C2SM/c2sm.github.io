---
date:
  created: 2026-10-19
categories:
  - Climate Model & Data
---

# New tool: Data Compression Toolkit (dc_toolkit)

The [Data Compression Toolkit](../tools/dc_toolkit.md) is now part of the C2SM tools. It helps you find the optimal compression setup for your netCDF data while staying within customized error budgets.

<!-- more -->

### What it does

The dc_toolkit tests all combinations of serializers, filters and compressors on a representative sample of each field, keeps only the pipelines that respect your L1, L2 or L∞ error thresholds, and writes the data into a Zarr store using the best one. After compression, every field is read back and checked against the original thresholds. Instead of manual thresholds, the [ESiWACE3 community recommendations :material-open-in-new:](https://compression-recommendations.readthedocs.io){:target="_blank"} for ERA5 variables can be used.

The toolkit runs on Santis, Balfrin, and Euler, and scales across many nodes with `srun`.

### Related links

- [dc_toolkit page](../tools/dc_toolkit.md)
- [Data compression best practices](../best_practices/data_handling/compression.md)
- [Repository at C2SM :material-open-in-new:](https://github.com/C2SM/data-compression){:target="_blank"}
