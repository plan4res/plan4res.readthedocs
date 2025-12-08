### Running the SSV module

The SSV module can be launched as follows:

> p4r SSV YourDataset

This module will compute optimal strategies for the management of
seasonal storages, which are defined as Bellman Values. The FORMAT
module must have been ran before (to produce the NetCDF files)

**Inputs**: SDDPBlock.nc4 and Block\$i.nc4 (\$i are indexes of SSV
timesteps), in nc4_optim/

**Outputs**: BellmanValuesOUT.csv and cuts.txt (BellmanValuesOUT.csv is
created only if the sddp has reached convergence; cuts.txt exists as
soon as it has completed at least one iteration), in results_optim/. See
the format of these files in section

SSV requires the following **configuration files**:

-   Plan4res.yml (see

-   The SMS++ configuration files sddp_solver.txt and
    uc_solverconfig.txt. These configuration file is updated by the SSV
    module. See section **Erreur ! Source du renvoi introuvable.** for
    more details.

SSV can be re-ran in hot-start (ie using the current solution as a
starting point) when adding option -H: p4r SSV YourDataSet -H

SSV can also be ran in 2 steps, using option -S. this allows to decrease
the computation time. The parameters of -S
(**NumberIterationsFirstStep** and **CheckConvEachXIter** ) can be
passed either via the p4r command: p4r SSV YourDataSet -S
NumberIterationsFirstStep CheckConvEachXIter, or in the
plan4res_settings configuration file (p4r SSV YourDataSet -S). The 2
steps of SSV are: a first step with maximum NumberIterationsFirstStep
iterations, in which the convergence is checked each
**CheckConvEachXIter** iteration, and a second step which is using the
parameters defined in sddp_solver.txt. Checking the convergence takes
some time, as it means simulating some scenarios, and it may not be
necessary to do it often in the first iterations, which is why this
option may save computation time.

