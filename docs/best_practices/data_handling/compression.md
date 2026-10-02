# Data Compression

Compression can considerably reduce disk space usage and the time needed for data transfer. However, compressing and decompressing data consumes CPU and memory resources and can slow down read and write operations.

!!! tip "When to compress"
    Ideally, compress data that is not accessed frequently. Compression is highly recommended for data that is stored in an archive (see [Archiving Data](recommendations.md#6-archiving-data)).

## Lossless vs. lossy compression

| | Lossless | Lossy |
|---|---|---|
| **Principle** | Restores the file to its original state, without the loss of a single bit | Permanently removes bits that are redundant, unimportant, or imperceptible |
| **Typical use** | Measured and simulated data, archives | Graphics, audio, video, images; depending on the use case also measured or simulated data |
| **Reversible** | :material-check: Yes | :material-close: No |
| **File size** | Smaller | Usually smallest |

## Working with compressed files

Compressed files such as `*.gz`, `*.zip`, or `*.bz2` normally need to be uncompressed before they can be used again. There are alternatives, however:

- Linux commands such as `zless`, `zcat`, `zdiff`, and `zgrep` handle compressed files on the fly.
- Scripting languages such as R, Python, Matlab, or IDL can read compressed files directly.

## Standard lossless methods

!!! success "Recommendation"
    We recommend **lossless compressed netCDF4** files for most use cases. The netCDF4 library, and all tools compiled with netCDF4 support, integrate compression seamlessly.

Lossless compression in netCDF4 is based on the zlib library. The following parameters can be tuned:

- **Compression level**: ranges from 1 (least aggressive) to 9 (most aggressive). Level 1 requires moderate CPU and memory resources and is sufficient for most purposes. Higher levels usually produce smaller files, but at a higher processing cost when packing and unpacking.
- **Chunk sizes**: compression operates on data chunks. These should match the data blocks that are typically accessed at the same time.
- **Shuffling**: often further reduces the data size.
- **Unlimited dimensions**: remove unneeded unlimited dimensions, as they may reduce the compression efficiency.

### Tools

=== "nccopy"

    Part of every netCDF4 installation. Allows setting the compression level, the shuffling option, and chunk sizes.

    ```bash
    # Compression level 1 with shuffling
    nccopy -d 1 -s input.nc output.nc

    # Additionally set chunk sizes per dimension
    nccopy -d 1 -s -c time/1,lat/180,lon/360 input.nc output.nc
    ```

=== "NCO (ncks)"

    The `ncks` command is part of the [NCO :material-open-in-new:](https://nco.sourceforge.net/nco.html){:target="_blank"} toolkit and offers extensive chunking options.

    ```bash
    ncks -4 -L 1 input.nc output.nc
    ```

    !!! info "IAC systems"
        On IAC systems, the script `nczip` is installed. It is a wrapper around `ncks` and compresses or decompresses a single netCDF file or all netCDF files in a folder.

=== "CDO"

    [Climate Data Operators :material-open-in-new:](https://code.mpimet.mpg.de/projects/cdo){:target="_blank"} can compress netCDF files, but offer fewer chunking options than NCO.

    ```bash
    cdo -f nc4 -z zip_1 copy input.nc output.nc
    ```

=== "nccompress"

    [nccompress :material-open-in-new:](https://github.com/coecms/nccompress){:target="_blank"} is another alternative to `nczip` for batch compression of netCDF files.

=== "Source code"

    Compression settings can also be specified directly in the source code when creating netCDF variables, e.g., via the Fortran, R, or Python interfaces.

    ```python
    # xarray
    ds.to_netcdf("output.nc", encoding={"temp": {"zlib": True, "complevel": 1, "shuffle": True}})
    ```

## Lossy algorithms

!!! warning "No general recommendation yet"
    Lossy compression of scientific data is still an area of active experimentation. We cannot make general recommendations at this point. Always be aware of what might be lost: the removed information **cannot be restored**.

In general, lossy compression results in smaller files than lossless compression. Available options include:

- **NCO**: `ncks` supports several lossy compression algorithms. More information can be found in the [NCO User Guide :material-open-in-new:](https://nco.sourceforge.net/nco.html){:target="_blank"}.
- **Python**: [netcdf4-python :material-open-in-new:](https://unidata.github.io/netcdf4-python/){:target="_blank"} and [xarray :material-open-in-new:](https://docs.xarray.dev/en/stable/user-guide/io.html){:target="_blank"} support both lossless and lossy compression. Lossy compression is enabled by defining a *least significant digit*, i.e., the power of ten of the smallest decimal place in the data that is still reliable. All information below this threshold is removed before saving.
- **C2SM data-compression toolkit**: the [data-compression :material-open-in-new:](https://github.com/C2SM/data-compression){:target="_blank"} repository provides tools to explore compression techniques on your own data.
