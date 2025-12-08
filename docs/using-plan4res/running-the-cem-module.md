### Running the CEM module

#### Simple run of CEM

The CEM module can be launched as follows:

> p4r CEM YourDataset

This module will compute an optimized installed capacity (including also
adapting the capacity of short term storages and of interconnections)
and then simulate the optimal operation of this adapted power system
over the whole period. The SSV module and the FORMAT module must have
been ran before (to produce the NetCDF files and the Bellman Values).

**Inputs**:

-   InvestmentBlock.nc4, SDDPBlock.nc4, Block\$i.nc4, and (\$i are
    indexes of SSV timesteps), in nc4_invest/

-   BellmanValuesOUT.csv or cuts.txt in results_optim/

-   the csv files in csv_invest and csv_simul when running with option
    -L

**Outputs**: (in results_invest/)

-   Adapted system: Solution_OUT.csv

-   Optimal schedules of all assets: files ActivePower\$i.csv,
    Primary\$i.csv, Secondary\$i.csv,

-   Marginal costs: MarginalCostActivePowerDemand\$i.csv,
    MarginalCostPrimary\$i.csv MarginalCostSecondary\$i.csv
    MarginalCostInertia\$i.csv MarginalCostFlows\$i.csv

-   Volumes of all reservoirs (seasonal and short-term): Volume\$i.csv,

-   Flows in all lines: Flows\$i.csv

CEM requires the following **configuration files**:

-   Plan4res.yml (see

-   The SMS++ configuration files BSPar-investment.txt and
    uc_solverconfig.txt. These configuration file are updated by the CEM
    module. See section **Erreur ! Source du renvoi introuvable.** for
    more details.

CEM can be re-ran in hot-start (ie using the current solution as a
starting point) when adding othe ption -H: p4r CEM YourDataSet -H

The option -E epsilon allows to specify the convergence criteria of CEM.
Epsilon may also be passed in plan4res_settings.yml.

#### Complex runs of CEM

CEM may also be ran with additional options which allow to:

-   **Recompute the bellman values every N iterations of the capacity
    expansion algorithm**:

p4r CEM YourDataset -L

CEM -L is equivalent to running an algorithm composed of a number of
iterations where in each iteration CEM is ran, its outputs are used to
compute a new dataset (i.e. new files in csv_invest and csv_simul
accounting for the results of the CEM run, and new NetCDF files in
nc4_optim based on the new CSV files), and SSV is ran to compute new
Bellman Values which will be used in the next iteration.

The parameters of -L (**NumberOfCemIterations** and
**MaxNumberOfLoops**) can be passed either via the p4r command: p4r CEM
YourDataSet -L NumberOfCemIterations MaxNumberOfLoops, or in the
plan4res_settings configuration file (p4r CEM YourDataSet -L).
**NumberOfCemIterations** is the maximum number of iterations in each
run of CEM and **MaxNumberOfLoops** is the maximum number of iterations
SSV/CEM). If the parameters are available in both plan4res_settings.yml
and as arguments of the p4r command, the arguments of the command line
will be used.

CEM -L may also use the parameter **Distance** which can be passed via
the option -D distance, or via the plan4res_settings file. This
parameter allows to choose which convergence test is used when running
CEM with option -L: **distance** can be 2 (distance between initial
capacity and invested capacity is used for checking convergence) or 3
(distance between cost of investment solution at last 2 iterations is
used for checking convergence); if not provided, distance 2 is used.

-   **Launch in sequence the algorithm on different subsets of the
    scenarios**. This may be useful in case the computation time is too
    long with all scenarios. It will allow to compute a first result on
    e.g. 1 scenario, then hot-start the algorithm on a bigger subset of
    scenarios.

p4r CEM YourDataset -U list_scenarios.txt

This requires the additional configuration file: list_scenarios.txt.
This file gives on its first row the number of subsets of scenarios to
be used (it 2, it means that CEM will be launched twice), and on the
following rows, one subset is to be described in each row, with the
format \['scenario1','scenario2'\] (Here we assume that we are defining
a subset with 2 scenarios, and that the scenarios are named 'scenario1'
and 'scenario2'. Don't forget the quotes.....

