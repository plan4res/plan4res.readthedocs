# Plan4res outputs

The results of plan4res are detailed in the following subsections

The SSV runs a Stochastic Dynamic Dual Programming (SDDP) algorithm to compute Bellman values for all the seasonal storages.

**Note**: Bellman values represent the *cost-to-go functions* = the expected economic value associated to the various levels of the seasonal storages at each time stages. They are usually represented as sets of hyperplanes called *cuts*.

The results are:

- When the convergence criteria of the SDDP algorithm is metSee the plan4res run guide for more information.: *

  - BellmanValuesOUT.csv: redundant cuts have been pruned out.

  - BellmanValuesAllOUT.csv: contains all the cuts found by the algorithm.

- In any case, ie even without convergence: cuts.txt, which contains all the cuts already found by the SDDP algorithm. This is useful to help reach convergence since it is possible to launch the SSV again using the cuts from a previous run stored in cuts.txt as a hot start.

The format of this file is, as shown in Table 13, aiming to represent a polyhedral function at each SSV timestep. The first column (Timestep) gives the index of the SSV Timestep. There are a number of rows for each timestep, representing the different ‘cuts’ of the function at this timestep. The function at timestep $i is: $\max_{cuts}\left( \sum_{j = 0}^{R}{a\_ j} + b \right)$, where a_j and b are the values in the corresponding columns, and R is the number of reservoirs (the number of columns a_j).

Table 13: BellmanValuesOUT.csv

| 0110110110110113.9825E+1011011-113.4094411-1000011-10000117.4137E+1011011-113.4094411-1000011-81.517916111.2033E+1111011-81.78606611-311-150.94929115.6955E+1011011-0.03611-3.81611-8115.3972E+1011011-811-311-113.20533115.5282E+1011011-0.0324911-0.0324911-8115.4175E+1011011-0.03611-1000011-81.517916111.1965E+1111011-0.03611-811-81.517916115.5241E+10111110110110113.9637E+1011111-113.4094411-1000011-10000111.3613E+11 |

|---|

|  |  |  |

|  |

The simulation produces 2 sets of results:

- Raw results of the simulation. They correspond to the outputs of the model, without any post-treatment (the post-treatment is performed when running POSTTREAT).

- Post-treated results. These are results computed by the POSTTREAT function of plan4res.

All row results follow the same format: the index column gives the indexes of the simulation timesteps, while the other columns give the values corresponding to the name in the header (which can be a region, a technology….)

For each scenario $i, the following files are produced.

- Demand_Scen$i_OUT.csv: 1 column per node with the power demand in the node.

- ActivePower_Scen$i_OUT.csv: generation schedules. 1 column per unit (apart from the Seasonal Storage units which are duplicated in 2 columns: one for the generation part, and the other one for the pumping part). Note that all other units with storages comprise a unique column with both positive and negative (pumping) values.

- Primary_Scen$i_OUT.csv: primary reserve schedules. 1 column per unit (apart from the Seasonal Storage units which are duplicated in 2 columns: one for the generation part, and the other one for the pumping part).

- Secondary_Scen$i_OUT.csv: secondary reserve schedules. 1 column per unit (apart from the Seasonal Storage units which are duplicated in 2 columns: one for the generation part, and the other one for the pumping part)

- Inertia_Scen$i_OUT.csv : inertia provided by each unit. 1 column per unit (apart from the Seasonal Storage units which are duplicated in 2 columns: one for the generation part, and the other one for the pumping part).

- Volume_Scen$i_OUT.csv: volumes of each storage (seasonal storages and short-term storages).

- Flows_Scen$i_OUT.csv: flows between zones. 1 column per transmission line.

- MarginalCostActivePowerDemand_Scen$i_OUT.csv: marginal costs of the demand constraint. 1 column per node (ch the *ActivePowerDemand* constraint is always applied to Nodes).

- MarginalCostPrimary_Scen$i_OUT.csv: marginal costs of the primary reserve constraint. 1 column per region (at the partition level of the *PrimaryDemand* constraints, note that these constraints may apply to different regional partitions than the Demand. See section **Erreur ! Source du renvoi introuvable.**).

- MarginalCostSecondary_Scen$i_OUT.csv: marginal costs of the secondary reserve constraint. 1 column per zone (at the partition level of the *SecondaryDemand* constraints).

- MarginalCostInertia_Scen$i_OUT.csv: marginal costs of the Inertia constraint (at the partition level of the *InertiaDemand* constraints). 1 column per zone.

- MarginalCostFlows_Scen$i_OUT.csv: marginal costs of the lines. 1 column per line.

- MaxPower_Scen$i_OUT.csv: maximum available power. 1 column per technology.

**All files share the same format: a header containing the names of the series, an index with the time steps.**

***InstalledCapacity.csv and AggrInstalledCapacity.csv***: installed capacities (aggregated installed capacity, with aggregations such as defined in settingsPostTreatPlan4res.py) in the different available technologies per zone. 1 column per technology, 1 row per node. (the generation units are attached to nodes)

Table 14: InstalledCapacity.csv

| 011RoGonDor1125814.051119573.51116445.95488115339.7840931183694.002311DolAmroth115524.23944411367.121111.92339211011200011Harad11600011469.1416144111783.3719511101115000 |

|---|

|  |  |  |

|  |

***Generation.csv and AggrGeneration.csv***: total average (on scenarios) generation on the whole simulation time horizon (aggregated generation, with aggregations such as defined in settingsPostTreatPlan4res_XXX.py) from the different available technologies per node. 1 column per technology, 1 row per node. Note that the Non Served column corresponds to the non-served electricity.

Table 15: AggrGeneration.csv

| 011RoGonDor1112685038911578839017111858133111101124985210311DolAmroth1129932305.81126161752.21111697614.5112944912.111129463408.711Harad1137280301.61110847753.511117436876114098421.1411346617336 |

|---|

|  |  |  |

|  |

***Generation-NODE.csv*** and ***AggrGeneration-NODE.csv***: average generation (aggregated generation) from the different available technologies per node. 1 file per node, 1 column per technology, 1 row per simulation time step.

Table 16: Generation-Harad.csv

| 01102/07/203011886.92103091111259.398751142800.926811103/07/20301101111259.398751142800.926811104/07/20301101111259.398751142800.926811105/07/20301101111259.398751142800.926811106/07/20301101111259.398751142800.926811107/07/20301101111259.398751142800.926811108/07/20301101111259.398751142800.926811109/07/20301119775.914821111259.398751142800.92681 |

|---|

|  |  |  |

|  |

***Generation-NODE-$i.csv***: generation from the different available technologies in the node for scenario $i. 1 file per zone and scenario, 1 column per technology, 1 row per time step.

***Slack-ZONE.csv***: electricity not served per node. 1 file per node. 1 column per scenario, 1 row per time step.

Table 17: Slack-Harad.csv

| 01102/07/20301101101101101103/07/20301101101101101104/07/20301101101101101105/07/20301101101101101106/07/20301101101101101107/07/2030110110110110 |

|---|

|  |  |  |

|  |

***nbHoursSlack.csv***: number of hours with non-served electricity per node and scenario.

***MeanVariableCost.csv***: average variable costs. 1 column per node, 1 row per technology.

Table 18: MeanVariableCost.csv

| 011Hydro|Reservoir11011011011Biomass|w/o CCS1101111237784.61115639575.111Coal|Hard coal|w/o CCS1133024883611305191.1421146738612.111Coal|Lignite|w/o CCS11107785456110110 |

|---|

|  |  |  |

|  |

***VariableCostPerScenario.csv***: variable costs. 1 column per scenario and node, 1 row per techno.

Table 19: VariableCostPerScenario.csv

| 011Hydro|Reservoir11011011011011011Biomass|w/o CCS1101101101101111073780.1 |

|---|

|  |  |  |

|  |

***meanScenCmar.csv***: average over all scenarios of the marginal costs. 1 column par node, 1 row per time step.

Table 20: meanScenCmar.csv

| 01102/07/2030110.0361181181.5179161103/07/2030110.036117.4151181.5179161104/07/2030110.0361181181.5179161105/07/2030110.036115.9996481181.5179161106/07/2030110.036115.9996481181.5179161107/07/2030110.036115.9996481177.54391761108/07/2030110.036115.9996481181.5179161109/07/2030110.0361181181.5179161110/07/2030110.0361181181.5179161111/07/2030110.036115.9996481181.517916 |

|---|

|  |  |  |

|  |

***meanTimeCmar.csv***: average over all timesteps of the marginal costs. 1 column per node, 1 row per scenario.

Table 21: meanTimeCmar.csv

| 011Base11256.72732113439.75537111521.5479311PVminus1011257.017259113583.34174111793.5726411Demandplus1011442.220462114878.66198113086.8707211PVminus10AndDemandplus1011451.32022114977.57685113259.88472 |

|---|

|  |  |  |

|  |

***sortedCmar.csv***: average of the marginal costs histogram. 1 column par node, 1 row per sorted time step index.

Table 22: SortedCmar.csv

| 0110111000011100001110000111111000011100001110000112111000011100001110000113111000011100001110000114119512.511100001110000115119154.8808911100001110000116119154.8808911100001110000117118749.7811100001110000118118506.0311100001110000 |

|---|

|  |  |  |

|  |

***MarginalCostActivePowerDemand-NODE.csv***: marginal costs of the node (in this case, the nodes on which the *ActivePowerDemand* constraints apply). 1 column par scenario, 1 row per time step.

***HistCmar-NODE.csv*** : histogram of the marginal costs of the zone. 1 column par scenario, 1 row per sorted time step index.

***MeanImportExport-NODE.csv***: average import and exports to/from the node. 1 column for Import, 1 column for export, 1 row per time step.

Table 23: meanImportExport-NODE.csv

| 01102/07/203011011224881103/07/203011011224881104/07/203011011224881105/07/203011011224881106/07/203011011224881107/07/20301101122488 |

|---|

|  |  |  |

|  |

***ImportExport-NODE-$i.csv***: import and exports to/from the node for scenario $i. 1 column for import, 1 column for export, 1 row per time step.

***MeanImportExport.csv***: average flows. 1 column for import, 1 column for line, 1 row per time step.

Table 24: MeanImportExport.csv

| 01102/07/2030111704115280011207841103/07/2030111704115280011207841104/07/2030111704115280011207841105/07/2030111704115280011207841106/07/2030111704115280011207841107/07/203011170411528001120784 |

|---|

|  |  |  |

|  |