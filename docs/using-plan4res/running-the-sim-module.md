### Running the SIM module

The SIM module can be launched as follows:

> p4r SIM YourDataset

This module will simulate the optimal operation of the power system over
the whole period. The SSV module and the FORMAT module must have been
ran before (to produce the NetCDF files and the Bellman Values). It will
compute the optimal schedules for each asset in all the regions for all
the scenarios, as well as the marginal costs of all the coupling
constraints in all the regions and for the interconnections.

**Inputs**:

-   SDDPBlock.nc4, Block\$i.nc4, and InvestmentBlock.nc4 (\$i are
    indexes of SSV timesteps), in nc4_simul/

-   BellmanValuesOUT.csv or cuts.txt in results_optim/

**Outputs**: (in results_simul/)

-   Optimal schedules of all assets: files ActivePower\$i.csv,
    Primary\$i.csv, Secondary\$i.csv,

-   Marginal costs: MarginalCostActivePowerDemand\$i.csv,
    MarginalCostPrimary\$i.csv MarginalCostSecondary\$i.csv
    MarginalCostInertia\$i.csv MarginalCostFlows\$i.csv

-   Volumes of all reservoirs (seasonal and short-term): Volume\$i.csv,

-   Flows in all lines: Flows\$i.csv

SIM requires the following **configuration files**:

-   Plan4res.yml (see

-   The SMS++ configuration files BSPar-investment.txt, sddp_greedy.txt,
    sddp_greedy_investment.txt and uc_solverconfig.txt. These
    configuration file is updated by the SSV module. See section
    **Erreur ! Source du renvoi introuvable.** for more details.

