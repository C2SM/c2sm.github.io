# Run Probtest on Säntis

Use Probtest to verify whether your test case produces consistent results on GPU. It compares a GPU test run to a CPU ensemble with perturbed input conditions.

## 1. Compile ICON
Compile ICON on CPU and on GPU as [out-of-source builds](compile_and_run.md#building-out-of-source). Note that the build directories need to be sub-directories of the ICON root folder. Otherwise the probtest container does not have access to the data.

## 2. Set Up the Probtest Container and Environment on Säntis
To run Probtest for ICON on Säntis, use the prebuilt container available on Docker Hub ([Probtest Container :material-open-in-new:](https://github.com/MeteoSwiss/probtest?tab=readme-ov-file#probtest-container){:target="_blank"}). ICON provides the wrapper script [`probtest_container_wrapper.py` :material-open-in-new:](https://gitlab.dkrz.de/icon/icon-nwp/-/blob/ci_probtest/scripts/cscs_ci/probtest_container_wrapper.py?ref_type=heads){:target="_blank"}.

!!! note
    If your ICON version doesn’t include this script, add it to `scripts/cscs_ci/probtest_container_wrapper.py`, along with the appropriate [PROBTEST_TAG :material-open-in-new:](https://gitlab.dkrz.de/icon/icon-nwp/-/blob/ci_probtest/run/tolerance/PROBTEST_TAG?ref_type=heads){:target="_blank"} under `run/tolerance/PROBTEST_TAG` and [yaml_experiment_test_processor.py :material-open-in-new:](https://gitlab.dkrz.de/icon/icon-nwp/-/blob/ci_probtest/scripts/experiments/yaml_experiment_test_processor.py?ref_type=heads){:target="_blank"} under `scripts/experiments/yaml_experiment_test_processor.py` (replace if already available).


### When Setting Up ICON from scratch
In your ICON root directory, import the containter:

```console
PROBTEST_TAG=$(cat run/tolerance/PROBTEST_TAG)
enroot import docker://c2sm/probtest:${PROBTEST_TAG}
```

Add a TOML configuration and export EDF path (being used when running the container):
```console
echo "image = \"$(pwd)/c2sm+probtest+${PROBTEST_TAG}.sqsh\"" > probtest.toml
echo "mounts = [ \"$(pwd)\" ]" >> probtest.toml
echo "workdir = \"$(pwd)\"" >> probtest.toml
echo "writable = true" >> probtest.toml
export EDF_PATH=$(pwd)
```

Create and activate Python environment:
```console
python3 -m venv .venv
source .venv/bin/activate
pip install pyyaml pandas click toml
```

### Every Time You Reconnect to the Server
If the container and environment are already set up, simply re-run:
```console
export EDF_PATH=$(pwd)
source .venv/bin/activate
```

Set experiment name, e.g.:
```console
export EXPERIMENT=c2sm_clm_r13b03_seaice
```

Export required environment variables:
```console
export BB_NAME=santis_cpu_nvhpc
export UENV_VERSION=$(cat config/cscs/SANTIS_ENV_TAG)
```

## 3. Run perturbed ensemble on CPU
Navigate to your CPU build directory and generate and run a 10-member ensemble (this may take time):
```console
./make_runscripts $EXPERIMENT
uenv run ${UENV_VERSION} -- python3 scripts/cscs_ci/probtest_container_wrapper.py ensemble $EXPERIMENT --build-dir $(pwd) --member-ids $(seq -s, 1 10)
```

This generates:

- `stats_${EXPERIMENT}_<member_id>.csv`
- `${EXPERIMENT}_reference.csv`

## 4. Generate Reference and Tolerance from Ensemble

Create reference and tolerance files using the 10 ensemble members:
```console
python3 scripts/cscs_ci/probtest_container_wrapper.py tolerance $EXPERIMENT --build-dir $(pwd) --member-ids $(seq -s, 1 10)
```

This generates:

- `${EXPERIMENT}_tolerance.csv`

## 5. Run the test case on GPU and collect statistics
In the following, replace `<...>` by the corresponding paths you are using.

Navigate to your GPU build folder and run the same test case, e.g.:
```console
cd <path-to-GPU-build>
./make_runscripts $EXPERIMENT
cd run && sbatch --uenv ${UENV_VERSION} ./exp.c2sm_clm_r13b03_seaice.run
```

Navigate back to ICON root folder and collect the GPU statistics:
```console
cd <ICON root folder>
python3 scripts/cscs_ci/probtest_container_wrapper.py stats $EXPERIMENT --stats-file-path <path-to-CPU-build>/stats_gpu.csv --build-dir <path-to-GPU-build>
```

This saves the GPU stats as `stats_gpu.csv` in your CPU build directory.

## 6. Check GPU Statistics Against Reference and Tolerance

From your ICON directory, run the check using the generated reference and tolerance:
```console
python3 scripts/cscs_ci/probtest_container_wrapper.py check $EXPERIMENT --input-file-cur stats_gpu.csv --input-file-ref <path-to-CPU-build>/${EXPERIMENT}_reference.csv --tolerance-file-name <path-to-CPU-build>/${EXPERIMENT}_tolerance.csv --build-dir $(pwd)
```

## 7. Increase Ensemble Size if Validation Fails
A 10-member ensemble may not capture the full variability, causing false negatives. Increase to 49 members for better coverage from your CPU build directory:

Run additional members (11–49):
```console
./make_runscripts $EXPERIMENT
uenv run ${UENV_VERSION} -- python3 scripts/cscs_ci/probtest_container_wrapper.py ensemble $EXPERIMENT --build-dir $(pwd) --member-ids $(seq -s, 11 49)
```

Regenerate reference and tolerance using all 49 members:
```console
python3 scripts/cscs_ci/probtest_container_wrapper.py tolerance $EXPERIMENT --build-dir $(pwd) --member-ids $(seq -s, 1 49)
```

*If the test still fails, the GPU result is likely incorrect.*