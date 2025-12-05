# Running the plan4res optimization modules SSV, SIM and CEM

These 3 modules are the main components of plan4res. They correspond to executables of the SMS++ library. They are all launched using p4r MODULE YourDataSet. A number of options can be added to this command (see section 5.1.1), in particular -C (to force use of CREATE first) and -F (to force use of FORMAT first) and -o Dir (to write the results in a sub-directory Dir of results_XXX/) . Some of these options (see below) allow to pass parameters, which can also be included in the plan4res_settings.yml configuration file. Whenever a parameter is present in the configuration file and via an option of p4r, the value which will be used is the one in the option of p4r.

The SSV module can be launched as follows:

p4r SSV YourDataset

This module will compute optimal strategies for the management of seasonal storages, which are defined as Bellman Values. The FORMAT module must have been ran before (to produce the NetCDF files)

**Inputs**: SDDPBlock.nc4 and Block$i.nc4 ($i are indexes of SSV timesteps), in nc4_optim/

**Outputs**: BellmanValuesOUT.csv and cuts.txt (BellmanValuesOUT.csv is created only if the sddp has reached convergence; cuts.txt exists as soon as it has completed at least one iteration), in results_optim/. See the format of these files in section

SSV requires the following **configuration files**:

- Plan4res.yml (see

- The SMS++ configuration files sddp_solver.txt and uc_solverconfig.txt. These configuration file is updated by the SSV module. See section **Erreur ! Source du renvoi introuvable.** for more details.

SSV can be re-ran in hot-start (ie using the current solution as a starting point) when adding option -H: p4r SSV YourDataSet -H

SSV can also be ran in 2 steps, using option -S. this allows to decrease the computation time. The parameters of -S (**NumberIterationsFirstStep** and **CheckConvEachXIter** ) can be passed either via the p4r command: p4r SSV YourDataSet -S NumberIterationsFirstStep CheckConvEachXIter, or in the plan4res_settings configuration file (p4r SSV YourDataSet -S). The 2 steps of SSV are: a first step with maximum NumberIterationsFirstStep iterations, in which the convergence is checked each **CheckConvEachXIter** iteration, and a second step which is using the parameters defined in sddp_solver.txt. Checking the convergence takes some time, as it means simulating some scenarios, and it may not be necessary to do it often in the first iterations, which is why this option may save computation time.

The SIM module can be launched as follows:

p4r SIM YourDataset

This module will simulate the optimal operation of the power system over the whole period. The SSV module and the FORMAT module must have been ran before (to produce the NetCDF files and the Bellman Values). It will compute the optimal schedules for each asset in all the regions for all the scenarios, as well as the marginal costs of all the coupling constraints in all the regions and for the interconnections.

**Inputs**:

- SDDPBlock.nc4, Block$i.nc4, and InvestmentBlock.nc4 ($i are indexes of SSV timesteps), in nc4_simul/

- BellmanValuesOUT.csv or cuts.txt in results_optim/

**Outputs**: (in results_simul/)

- Optimal schedules of all assets: files ActivePower$i.csv, Primary$i.csv, Secondary$i.csv,

- Marginal costs: MarginalCostActivePowerDemand$i.csv, MarginalCostPrimary$i.csv MarginalCostSecondary$i.csv MarginalCostInertia$i.csv MarginalCostFlows$i.csv

- Volumes of all reservoirs (seasonal and short-term): Volume$i.csv,

- Flows in all lines: Flows$i.csv

SIM requires the following **configuration files**:

- Plan4res.yml (see

- The SMS++ configuration files BSPar-investment.txt, sddp_greedy.txt, sddp_greedy_investment.txt and uc_solverconfig.txt. These configuration file is updated by the SSV module. See section **Erreur ! Source du renvoi introuvable.** for more details.

The CEM module can be launched as follows:

p4r CEM YourDataset

This module will compute an optimized installed capacity (including also adapting the capacity of short term storages and of interconnections) and then simulate the optimal operation of this adapted power system over the whole period. The SSV module and the FORMAT module must have been ran before (to produce the NetCDF files and the Bellman Values).

**Inputs**:

- InvestmentBlock.nc4, SDDPBlock.nc4, Block$i.nc4, and ($i are indexes of SSV timesteps), in nc4_invest/

- BellmanValuesOUT.csv or cuts.txt in results_optim/

- the csv files in csv_invest and csv_simul when running with option -L

**Outputs**: (in results_invest/)

- Adapted system: Solution_OUT.csv

- Optimal schedules of all assets: files ActivePower$i.csv, Primary$i.csv, Secondary$i.csv,

- Marginal costs: MarginalCostActivePowerDemand$i.csv, MarginalCostPrimary$i.csv MarginalCostSecondary$i.csv MarginalCostInertia$i.csv MarginalCostFlows$i.csv

- Volumes of all reservoirs (seasonal and short-term): Volume$i.csv,

- Flows in all lines: Flows$i.csv

CEM requires the following **configuration files**:

- Plan4res.yml (see

- The SMS++ configuration files BSPar-investment.txt and uc_solverconfig.txt. These configuration file are updated by the CEM module. See section **Erreur ! Source du renvoi introuvable.** for more details.

CEM can be re-ran in hot-start (ie using the current solution as a starting point) when adding othe ption -H: p4r CEM YourDataSet -H

The option -E epsilon allows to specify the convergence criteria of CEM. Epsilon may also be passed in plan4res_settings.yml.

CEM may also be ran with additional options which allow to:

- **Recompute the bellman values every N iterations of the capacity expansion algorithm**:

p4r CEM YourDataset -L

CEM -L is equivalent to running an algorithm composed of a number of iterations where in each iteration CEM is ran, its outputs are used to compute a new dataset (i.e. new files in csv_invest and csv_simul accounting for the results of the CEM run, and new NetCDF files in nc4_optim based on the new CSV files), and SSV is ran to compute new Bellman Values which will be used in the next iteration.

The parameters of -L (**NumberOfCemIterations** and **MaxNumberOfLoops**) can be passed either via the p4r command: p4r CEM YourDataSet -L NumberOfCemIterations MaxNumberOfLoops, or in the plan4res_settings configuration file (p4r CEM YourDataSet -L). **NumberOfCemIterations** is the maximum number of iterations in each run of CEM and **MaxNumberOfLoops** is the maximum number of iterations SSV/CEM). If the parameters are available in both plan4res_settings.yml and as arguments of the p4r command, the arguments of the command line will be used.

CEM -L may also use the parameter **Distance** which can be passed via the option -D distance, or via the plan4res_settings file. This parameter allows to choose which convergence test is used when running CEM with option -L: **distance** can be 2 (distance between initial capacity and invested capacity is used for checking convergence) or 3 (distance between cost of investment solution at last 2 iterations is used for checking convergence); if not provided, distance 2 is used.

- **Launch in sequence the algorithm on different subsets of the scenarios**. This may be useful in case the computation time is too long with all scenarios. It will allow to compute a first result on e.g. 1 scenario, then hot-start the algorithm on a bigger subset of scenarios.

p4r CEM YourDataset -U list_scenarios.txt

This requires the additional configuration file: list_scenarios.txt. This file gives on its first row the number of subsets of scenarios to be used (it 2, it means that CEM will be launched twice), and on the following rows, one subset is to be described in each row, with the format [‘scenario1’,’scenario2’] (Here we assume that we are defining a subset with 2 scenarios, and that the scenarios are named ‘scenario1’ and ‘scenario2’. Don’t forget the quotes…..

This configuration file contains parameters for the plan4res modules SSV and CEM. Some of those parameters can be passed as options of the p4r command (in this case the value passed in option will always be used).

This file contains the following parameters:

- **SSV parameters**

- **NumberSSVIterationsFirstStep**: maximum number of iterations of the first step, when using option -S

- **NumberSSVIterations**: maximum number of iterations when not using option -S, or maximum number of iterations in the final step when using option -S

- **CheckConvEachXIterInFirstStep**: convergence is checked after X iterations of the sddp algorithm in the first step, when ran with option -S

- **CheckConvEachXIter**: convergence is checked after X iterations of the sddp algorithm in the unique SSV step when ran without option -S, and in final SSV step when ran with option -S

- **EpsilonSSV**: convergence criteria of SSV

- **CEM parameters**

- **NumberOfCemIterationsInLoopCEM**: maximum number of iterations in each run of CEM when CEM is launched with option -L

- **NumberOfCemIterations**: maximum number of iterations in each run of CEM when CEM is launched without option -L or in the last CEM run when launched with -L

- **MaxNumberOfLoops**: maximum number of iterations SSV/CEM when CEM is launched with option -L

- **EpsilonCEM**: convergence criteria for CEM when launched with option -L

- **Distance**: choice of the distance computation for CEM when launched with option -L. distance can be 2 or 3 -default 2- 2 means that the distance between the initial capacity and the invested capacity is used for checking convergence; 3 means that the distance between the cost of the investment solution at the last 2 iterations is used for checking convergence

- **ScenariosLists**: name of the configuration file for running CEM with option -U

These modules include complete workflows.

p4r SSVandSIM YourDataset does the following:

- If used with option -C: p4r CREATE YourDataset

- p4r FORMAT YourDataset -M optim

- p4r SSV YourDataset

- p4r FORMAT YourDataset -M simul

- p4r SIM YourDataset

- p4r POSTTREAT YourDataset

p4r SSVandCEM YourDataset does the following:

- If used with option -C: p4r CREATE YourDataset -M invest

- p4r FORMAT YourDataset -M optim -m invest

- p4r SSV YourDataset -M invest

- p4r FORMAT YourDataset -M invest

- p4r CEM YourDataset

- p4r POSTTREAT YourDataset -M invest