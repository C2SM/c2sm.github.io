# Run Probtest on Säntis

This guide shows how to run probtest to verify whether a GPU test run is consistent with a CPU ensemble run with perturbed input conditions. It does not check against the CI saved references.


## 1. Compile ICON
Compile ICON on CPU and on GPU as [out-of-source builds](compile.md#building-out-of-source) in sub-directories of ICON.

!!! note
    The probtest container uses the ICON root directory as its working directory and can therefore only access data within the ICON root directory. This is why the out-of-source builds need to be subdirectories of ICON.

## 2. Set Up the Probtest Container and Environment on Säntis
To run Probtest for ICON on Säntis, we use the prebuilt container available on Docker Hub ([Probtest Container :material-open-in-new:](https://github.com/MeteoSwiss/probtest?tab=readme-ov-file#probtest-container){:target="_blank"}).
!!! note
    Make sure your ICON version includes the appropriate [PROBTEST_TAG :material-open-in-new:](https://gitlab.dkrz.de/icon/icon-nwp/-/blob/master/run/tolerance/PROBTEST_TAG?ref_type=heads){:target="_blank"} under `run/tolerance/PROBTEST_TAG` and [yaml_experiment_test_processor.py :material-open-in-new:](https://gitlab.dkrz.de/icon/icon-nwp/-/blob/master/scripts/experiments/yaml_experiment_test_processor.py?ref_type=heads){:target="_blank"} under `scripts/experiments/yaml_experiment_test_processor.py`.


### When Setting Up ICON from Scratch
Add a TOML configuration to run the probtest container in your ICON root directory (this requires setting the `EDF_PATH` to your *current directory* = *ICON root directory*):
```console
PROBTEST_TAG=$(cat run/tolerance/PROBTEST_TAG)
echo "image = 'c2sm/probtest:${PROBTEST_TAG}'" > probtest.toml
echo "mounts = [ \"$(pwd)\" ]" >> probtest.toml
echo "workdir = \"$(pwd)\"" >> probtest.toml
echo "writable = true" >> probtest.toml
```

Install the Python image needed:
```
export UENV_NAME=$(cat config/cscs/SANTIS_ENV_TAG)
uenv run ${UENV_NAME} --view default -- bash -c 'python3 -m venv --clear .venv && source .venv/bin/activate && pip install click numpy pandas pyyaml toml'
```

### Every Time You Reconnect to the Server
If the `probtest.toml` file already exists in your ICON root directory, run the following command from within that directory:
```console
# Set the path to the probtest.toml file
export EDF_PATH=$(pwd)

# Set the builder name
export BB_NAME=santis_cpu_nvhpc

# Set the uenv version
export UENV_NAME=$(cat config/cscs/SANTIS_ENV_TAG)
```

Set experiment name, e.g.:
```console
export EXP=c2sm_clm_r13b03_seaice
```

## 3. Run perturbed ensemble on CPU and Generate Tolerance from Ensemble
To run a perturbed ensemble, please allocate compute nodes interactively to *not* use your login nodes. Therefore, run the following (replace `<project account>`):
```console
salloc -A <project account> -p normal --time=01:00:00
```

!!! warning "Compute account"
    Ensure that your default account at CSCS has computing resources. If this is not the case, you need to open a ticket 
    at the [CSCS Service Desk :material-open-in-new:](https://jira.cscs.ch/plugins/servlet/desk/site/global){:target="_blank"}.

Then navigate to your CPU build directory and run the `tolerance` task for a 10-member ensemble (this may take time):
```console
cd nvhpc_cpu
scripts/cscs_ci/run_local_ci.sh tolerance $EXP --build-dir $(pwd) --member-ids $(seq -s, 1 10)
```
This runs the ensemble, their stats and tolerance. It generates:

- `stats_${EXP}_<member_id>.csv`
- `${EXP}_reference.csv`
- `${EXP}_tolerance.csv`

## 5. Run the test case on GPU and collect statistics
Navigate to your GPU build folder and run the same test case, e.g.:
```console
cd ../nvhpc_gpu
./make_runscripts $EXP
cd run && uenv run $UENV_NAME --view modules,default -- bash -c './exp.$EXP.run 2>&1 | tee LOG.exp.$EXP.run.o' && cd ..
```

Navigate back to ICON root folder and collect the GPU statistics:
```console
cd ..
export PROBTEST_CONFIG="nvhpc_cpu/${EXP}-config.json"
srun --container-writable --environment=probtest \
    /probtest/probtest.py stats --no-ensemble --stats-file-name stats_gpu.csv \
    --model-output-dir ${EDF_PATH}/nvhpc_gpu/experiments/$EXP
```

This saves the GPU stats as `stats_gpu.csv` in your ICON root directory.

## 6. Check GPU Statistics Against Reference and Tolerance

From your ICON root directory, get the tolerance factor and run the check using the generated reference and tolerance:
```console
export PROBTEST_CONFIG="nvhpc_cpu/${EXP}-config.json"
FACTOR=$(uenv run "$UENV_NAME" --view modules,default -- \
        bash -c 'source .venv/bin/activate && scripts/experiments/get_param_for_exp_by_machine \
        --experiment "$EXP" --param tolerance_factor')

srun --container-writable --environment=probtest \
    /probtest/probtest.py check --current-files stats_gpu.csv --reference-files nvhpc_cpu/${EXP}_reference.csv     --tolerance-files nvhpc_cpu/${EXP}_tolerance.csv --factor "$FACTOR"
```

## 7. Increase Ensemble Size if Validation Fails
Again, if not done already, allocate compute nodes interactively to *not* use your login nodes:
```console
salloc -p normal --time=01:20:00
```

A 10-member ensemble may not capture the full variability, causing false negatives. Increase to 49 members for better coverage from your CPU build directory:

Run additional members (11–49):
```console
scripts/cscs_ci/run_local_ci.sh tolerance $EXP --build-dir $(pwd) --member-ids $(seq -s, 11 49)
```

*If the test still fails, the GPU result is likely incorrect.*