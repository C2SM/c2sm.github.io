# Data Compression Toolkit (dc_toolkit)

The [**dc_toolkit** :material-open-in-new:](https://github.com/C2SM/data-compression){:target="_blank"} automates the search for the best lossy compression pipeline for netCDF files and writes the result into a Zarr store. It sweeps all `compressor × filter × serializer` combinations on a representative sample of each field and filters the results according to predefined error thresholds.

For general guidance on lossless and lossy compression, see [Data Compression](../best_practices/data_handling/compression.md) in the best practices section.

## Key concepts

**Error metrics**:

- L1 (mean absolute error): average deviation across all cells; the most common budget for climate data.
- L2 (root-mean-square error): penalizes large local deviations.
- L∞ (maximum absolute error): the worst-case deviation anywhere in the field.
- Bias: positive and negative errors cancel each other out to maintain a balanced output
- q99 tail: checks outliers
- Physical bounds: min and max values for a field
- Finiteness: no NaN/infinite values introduced
- Gradient: spatial structure preserved

**Compression pipeline**: compression is applied in up to three stages:

| Stage          | Role | Examples |
|----------------|---|---|
| **Serializer** | Converts floating-point values into bytes | `zfp`, `EBCC`, `FixedScaleOffset` |
| **Filter**     | Pre-processes data to improve compressibility | `Delta`, `BitRound`, `AsType` |
| **Compressor** | Applies a byte-level codec | `Zstd`, `Blosc`, `LZ4` |

!!! info "Community recommendations"
    The ESiWACE3 project publishes [community recommendations :material-open-in-new:](https://compression-recommendations.readthedocs.io){:target="_blank"} specifying the maximum permissible error for ERA5 variables. These can be used as the gate of a sweep instead of manual error thresholds.

## Workflow

1. `evaluate_combos` sweeps the codec space on a sample of each field and writes the best pipeline into a JSON file. In this example, the relative L1 error budget is set to 0.5 %:

    ```bash
    dc_toolkit evaluate_combos input.nc \
      --where-to-write ./path_to_folder \
      --field-to-compress field \
      --l1-threshold 0.005 \
      --eval-data-size-limit 5GB
    ```

2. `compress` writes all fields into a shared `.zarr` store and re-reads every field to verify that the stored data meets the original thresholds:

    ```bash
    dc_toolkit compress input.nc ./out
    ```

## Compression libraries

- [Numcodecs :material-open-in-new:](https://numcodecs.readthedocs.io){:target="_blank"}: the standard Zarr codec library, providing Zstd, Blosc, LZ4, FixedScaleOffset, Delta, etc.
- [EBCC :material-open-in-new:](https://github.com/spcl/EBCC){:target="_blank"} *(optional)*: the Error Bounded Climate Compressor. At loose error bounds (0.1–1 % of the field's range) it achieves 2–4× the ratio of `zfp`; at tight bounds the advantage disappears. However, it is slow to encode (~1–2 MB/s per core).

## Installation

```bash
git clone https://github.com/C2SM/data-compression.git dc_toolkit
cd dc_toolkit
python -m venv venv && source venv/bin/activate
bash install_dc_toolkit.sh
```

## HPC usage

On Santis, load the `prgenv-gnu/26.3:v1` uenv first. On Balfrin, use `netcdf-tools/2024:v1`.

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

## Documentation

For further details, including Docker usage and a step-by-step walkthrough, see the [dc_toolkit documentation :material-open-in-new:](https://github.com/C2SM/data-compression){:target="_blank"}.
