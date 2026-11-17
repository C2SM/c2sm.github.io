# Run Test Case

In the *run* folder of your ICON root directory, you find many prepared test cases, which you can convert into run
scripts. To generate the runscript of one of the experiment files, you can use the `make_runscripts` function.

First, set experiment name, e.g.:

```console
export EXP=c2sm_clm_r13b03_seaice
```

Then, generate the runscript for your experiment:

```shell
./make_runscripts ${EXP}
```

To run the created runscript, navigate to the *run* subdirectory and submit the runscript.

=== "Santis"
    ```shell
    UENV_VERSION=$(cat config/cscs/SANTIS_ENV_TAG)
    cd run && sbatch --uenv ${UENV_VERSION} ./exp.${EXP}.run
    ```
=== "Euler"
    ```shell
    cd run && sbatch ./exp.${EXP}.run
    ```

    !!! warning "Run scripts fail with `MPI_ERR_COMM: invalid communicator`"
        In ICON `release-2026.10-public`, the run scripts for Euler start ICON with `srun`.
        Since Euler's Slurm does not support PMIx, which OpenMPI 5 requires, `srun` starts each MPI task
        as a separate single-task run (the log shows `ICON run on 1 mpi processes`), and the run aborts.
        As a workaround, replace `srun` with the `mpirun` of the Spack environment before submitting.
        Run the following from the ICON root folder (for an out-of-source build, use e.g. `cd gcc_cpu/run`):

        ```shell
        MPIRUN=$(realpath config/ethz/spack/euler_cpu_gcc/.spack-env/view/bin/mpirun)
        cd run && sed -i "s|START=\"srun -n|START=\"${MPIRUN} -n|" exp.${EXP}.run
        sbatch ./exp.${EXP}.run
        ```
=== "Balfrin"
    ```shell
    cd run && sbatch ./exp.${EXP}.run
    ```
=== "Eiger"
    ```shell
    cd run && sbatch ./exp.${EXP}.run
    ```
You may need to adjust the account in the runscript to match your permissions. Alternatively, you can include
`--account=<my_account_id>` in the `sbatch` command.
