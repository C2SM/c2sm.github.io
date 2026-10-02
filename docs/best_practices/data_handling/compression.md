# Data Compression

Compression can considerably reduce disk space usage and the time needed for data transfer. However, compressing and decompressing data consumes CPU and memory resources and can slow down read and write operations.

!!! tip "When to compress"
    Ideally, compress data that is not accessed frequently. Compression is highly recommended for data that is stored in an archive (see [Archiving Data](recommendations.md#6-archiving-data)).

## Lossless vs. lossy compression

| | Lossless | Lossy |
|---|---|---|
| Principle | Restores the file to its original state, without the loss of a single bit | Permanently removes bits that are redundant, unimportant, or imperceptible |
| Typical use | Measured and simulated data, archives | Graphics, audio, video, images; depending on the use case also measured or simulated data |
| Reversible | :material-check: Yes | :material-close: No |
| File size | Smaller | Usually smallest |

## Working with compressed files

Compressed files such as `*.gz`, `*.zip`, or `*.bz2` normally need to be uncompressed before they can be used again. There are alternatives, however:

- Linux commands such as `zless`, `zcat`, `zdiff`, and `zgrep` handle compressed files on the fly.
- Scripting languages such as R, Python, Matlab, or IDL can read compressed files directly.

## Standard lossless methods

!!! success "Recommendation"
    We recommend **lossless compressed netCDF4** files for most use cases. The netCDF4 library, and all tools compiled with netCDF4 support, integrate compression seamlessly.

Lossless compression in netCDF4 is based on the zlib library. The following parameters can be tuned:

- *Compression level*: ranges from 1 (least aggressive) to 9 (most aggressive). Level 1 requires moderate CPU and memory resources and is sufficient for most purposes. Higher levels usually produce smaller files, but at a higher processing cost when packing and unpacking.
- *Chunk sizes*: compression operates on data chunks. These should match the data blocks that are typically accessed at the same time.
- *Shuffling*: often further reduces the data size.
- *Unlimited dimensions*: remove unneeded unlimited dimensions, as they may reduce the compression efficiency.

### Tools

- **nccopy**

    Part of every netCDF4 installation. Allows setting the compression level, the shuffling option, and chunk sizes.

    ```bash
    # Compression level 1 with shuffling
    nccopy -d 1 -s input.nc output.nc

    # Additionally set chunk sizes per dimension
    nccopy -d 1 -s -c time/1,lat/180,lon/360 input.nc output.nc
    ```

- **NCO (ncks)**

    The `ncks` command is part of the [NCO :material-open-in-new:](https://nco.sourceforge.net/nco.html){:target="_blank"} toolkit and offers extensive chunking options.

    ```bash
    ncks -4 -L 1 input.nc output.nc
    ```

    !!! info "IAC systems"
        On IAC systems, the script `nczip` is installed. It is a wrapper around `ncks` and compresses or decompresses a single netCDF file or all netCDF files in a folder.

- **CDO**

    [Climate Data Operators :material-open-in-new:](https://code.mpimet.mpg.de/projects/cdo){:target="_blank"} can compress netCDF files, but offer fewer chunking options than NCO.

    ```bash
    cdo -f nc4 -z zip_1 copy input.nc output.nc
    ```

- **nccompress**

    [nccompress :material-open-in-new:](https://github.com/coecms/nccompress){:target="_blank"} is another alternative to `nczip` for batch compression of netCDF files.

- **Source code**

    Compression settings can also be specified directly in the source code when creating netCDF variables, e.g., via the Fortran, R, or Python interfaces.

    ```python
    import xarray as xr
    ds = xr.open_dataset("input.nc")
    ds.to_netcdf("output.nc", encoding={"temp": {"zlib": True, "complevel": 1, "shuffle": True}})
    ```

## Lossy algorithms

!!! warning "Use with care"
    Lossy compression permanently removes information that annot be restored. Always verify that the error introduced is acceptable for your use case before archiving or sharing data.

Lossy compression can achieve ratios of 10–50× for climate and weather data, far beyond what lossless methods offer. Available tools include:

- **NCO (ncks)**

    In addition to lossless compression (see [Standard lossless methods](#standard-lossless-methods)), `ncks` supports several lossy algorithms. 

- **Python**

    [netcdf4-python :material-open-in-new:](https://unidata.github.io/netcdf4-python/){:target="_blank"} and [xarray :material-open-in-new:](https://docs.xarray.dev/en/stable/user-guide/io.html){:target="_blank"} support lossy compression by defining a *least significant digit*. All information below this threshold is removed before saving.

- **C2SM dc_toolkit**

    The [data-compression :material-open-in-new:](https://github.com/C2SM/data-compression){:target="_blank"} toolkit systematically searches for the best compression pipeline for your data and verifies the result against a user-defined error threshold. See [C2SM data-compression toolkit](#c2sm-data-compression-toolkit) below.

## C2SM data-compression toolkit (dc_toolkit)

The [**dc_toolkit** :material-open-in-new:](https://github.com/C2SM/data-compression){:target="_blank"} automates the search for the best compression pipeline for netCDF files and writes the result into a zarr zip. It sweeps all `compressor × filter × serialiser` combinations on a representative sample of each field and filters results according to pre-defined error thresholds.

### Key concepts

**Error metrics**:

- L1 (mean absolute error): average deviation across all cells; the most common budget for climate data.
- L2 (root-mean-square error): penalises large local deviations.
- L∞ (maximum absolute error): the worst-case deviation anywhere in the field.

**Compression pipeline** — compression is applied in up to three stages:

| Stage | Role | Examples |
|---|---|---|
| Serialiser | Converts floating-point values into bytes | `zfp`, `EBCC`, `FixedScaleOffset` |
| Filter | Pre-processes data to improve compressibility | `Delta`, `BitRound`, `AsType` |
| Compressor | Applies a byte-level codec | `Zstd`, `Blosc`, `LZ4` |

Note: Community recommendations — the ESiWACE3 project publishes [community recommendations :material-open-in-new:](https://compression-recommendations.readthedocs.io){:target="_blank"} specifying the maximum permissible error for ERA5 variables. These can be used as the gate of a sweep as a replacement for manual error thresholds.

### Workflow

1. `evaluate_combos` — sweeps the codec space on a sample of each field and writes the best pipeline into a json file: 

```bash
dc_toolkit evaluate_combos input.nc \
  --where-to-write ./path_to_folder \
  --field-to-compress field \
  --l1-threshold 0.005 \        # relative L1 error budget (0.5 %)
  --eval-data-size-limit 5GB
```

2. `compress` — writes all fields into a shared `.zarr` store and re-reads every field to verify the stored data meets the original thresholds:

```bash
dc_toolkit compress input.nc ./out
```

### Compression libraries

- [Numcodecs :material-open-in-new:](https://numcodecs.readthedocs.io){:target="_blank"}: the standard Zarr codec library, providing Zstd, Blosc, LZ4, FixedScaleOffset, Delta, etc.
- [EBCC :material-open-in-new:](https://github.com/spcl/EBCC){:target="_blank"} *(optional)*: the Error Bounded Climate Compressor. At loose error bounds (0.1–1 % of the field's range) it achieves 2–4× the ratio of `zfp`; at tight bounds the advantage disappears. However, it is slow to encode (~1–2 MB/s per core).

### Installation

```bash
git clone https://github.com/C2SM/data-compression.git dc_toolkit
cd dc_toolkit
python -m venv venv && source venv/bin/activate
bash install_dc_toolkit.sh
```


### HPC usage
On santis, load the `prgenv-gnu/26.3:v1` uenv first. On balfrin, use `netcdf-tools/2024:v1`.

```bash
#SBATCH --nodes=8 --ntasks-per-node=32 --cpus-per-task=1

export OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 \
       BLOSC_NTHREADS=1 NUMBA_NUM_THREADS=1 \
       VECLIB_MAXIMUM_THREADS=1 OMP_THREAD_LIMIT=1

srun dc_toolkit evaluate_combos input.nc \
    --where-to-write ./out \
    --field-to-compress t \
    --l1-threshold 0.005 \
    --eval-data-size-limit 5GB
```

For further details, including Docker usage and a step-by-step walkthrough, see the [dc_toolkit documentation :material-open-in-new:](https://github.com/C2SM/data-compression){:target="_blank"}.