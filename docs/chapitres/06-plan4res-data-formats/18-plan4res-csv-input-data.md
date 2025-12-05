# Plan4res csv Input Data

This section describes the format of plan4res input data. A dataset is composed of 7 csv files representing the “fixed” data and of a number timeseries (described in section 6.2).

All the CSV input files are following.

1. 1

  

  

2. One row containing column labels

  Serie of Rows containing the data (consistent with column labels)

  Each row contains a name, a zone and various values of variables. Zone can be any level of geographical partition (see below).

**Columns that are not used may be skipped.**

**Important notice:** within plan4res, the convention for the units is that all data and results are in MW, MWh, €, €/MW, €/MWh depending on the variable (see **Erreur ! Source du renvoi introuvable.** **Erreur ! Source du renvoi introuvable.**)

The dataset is composed of:

- *ZP_ZonePartition.csv*: contains the description of the different regions;

- *ZV_ZoneValues.csv*: contains the data linked to the regions (in particular the demand);

- *IN_Interconnections.csv*: contains the description of the network;

- *TU_ThermalUnits.csv*: contains the description of the thermal power plants (including nuclear) and of any asset which can be modeled in plan4res as a thermal plant (even if not using any fossil fuel)

- *SS_SeasonalStorage.csv*: contains the description of hydropower with seasonal storages and other long-term seasonal storages;

- *STS_ShortTermStorage.csv*: contains the description of all the short-term storages, including eg. pumped hydro, batteries but it can also be used for demand-response mechanisms such as load-shifting;

- *RES_RenewableUnits.csv*: contains the description of PV, wind power and run-of-river technologies.

This first group of data files is used to describe the regions in the dataset, the interconnections between the regions, and the constraints at region level, such as the power demand, but also the system services.

The file ZP_ZonePartition.csv describes the different regions that are used in the dataset. In the example below, the lower level (on the left) corresponds to countries.

The lower level is used to define **Nodes**. Each generation unit (defined in TU_ThermalUnits.csv, RES_RenewableUnits.csv, STS_ShortTermUnits.csv and SS_SeasonalStorage.csv) belongs to one **Node**. Interconnections (defined in IN_Interconnections.csv) are connecting nodes.

The higher level corresponds to continents (with a unique continent called ‘MiddleEarth’). There could exist intermediate levels. The different levels are used to define “coupling constraints” (see ***Erreur ! Source du renvoi introuvable.** **Erreur ! Source du renvoi introuvable.***), such as the power demand which is always linked to a Node. Other coupling constraints (such as system services) may apply to different levels. (See ***Erreur ! Source du renvoi introuvable.** **Erreur ! Source du renvoi introuvable.*** for more details about regions)

Table 4: ZP_ZonePartition.csv

| 011RoGonDor11MiddleEarth11DolAmroth11MiddleEarth11Harad11MiddleEarth |

|---|

|  |  |  |

|  |

The different regions can be defined by the user in the settingsCreateInputPlan4res_*xxx*.yml configuration file (Regions section).

This file contains the values of all coupling constraints (in particular the demand at each Node, which is mandatory). It may also optionally contain the parameters for defining the costs associated to imbalance (for each coupling constraint). These parameters can also be defined in the settingsCreateInputPlan4res_*xxx*.yml configuration file (Coupling constraints section), in particular if the user wishes to use the same parameters for all the regions. If the user wishes to use different values, they must appear in ZV_ZoneValues.csv.

Table 5: ZV_ZoneValues.csv

| 011Cooking11DolAmroth117178950.65211TS_COOKING_DolAmroth.csv11ElecHeating11DolAmroth1154635950.1311TS_HEAT_LOW_DolAmroth.csv11ElecVehicle11DolAmroth1113541851.2611TS_MOBILITY_PSNG_DolAmroth.csv11OtherExclHeatTranspCooking11DolAmroth1151369219.8111TS_LOAD_DolAmroth.csv11CostActivePowerDemand11DolAmroth11100001111MaxActivePowerDemand11DolAmroth11150000011 |

|---|

|  |  |  |

|  |

Table 5 shows the content of ZV_ZoneValues.csv for the region “DolAmroth”. In this example, tere is only one type of coupling constraint per region, which is the power demand. The power demand is composed of 4 parts: power demand for cooking, for heating (ElecHeating), for transportation (ElecVehicle) and for other uses (OtherExclHeatTranspCooking). The unit of the values in the column ‘value’ is MWh or €/MWh (for the variables of Type Cost*). The row ‘Cooking’ gives in column ‘value’ the power demand for cooking in the region DolAmroth for the year, in MWh, as well as the name of the timeseries to use to compute the hourly power demand for cooking (here TS_COOKING_DolAmroth.csv). Whenever the timserie would be deterministic, the Profile_Timeserie column would contain the name of the column corresponding to this timeseries in the csv file containing all deterministic timeseries. Table 6 shows the first 6 hours of this timeseries, for the 3 scenarios ‘Base’, ‘PVminus10’ and ‘Demandplus10’). The (here scenarized) hourly power demand for cooking is computed by multiplying the timeseries by the numerical value in ZV_ZoneValue.csv.

Table 6: TS_COOKING_DolAmroth.csv

| 01101/01/2050 00:00111.60E-05111.60E-05111.76E-051101/01/2050 01:00111.60E-05111.60E-05111.76E-051101/01/2050 02:00111.60E-05111.60E-05111.76E-051101/01/2050 03:00111.60E-05111.60E-05111.76E-051101/01/2050 04:00111.60E-05111.60E-05111.76E-051101/01/2050 05:00111.60E-05111.60E-05111.76E-051101/01/2050 06:00113.31E-05113.31E-05113.64E-05 |

|---|

|  |  |  |

|  |

The total power demand (scenarized) timeseries of the region is computed by adding the 4 timeseries corresponding to the 4 parts of the power demand. The way of computing the power demand is defined in the settingsCreateInputPlan4res_*xxx*.yml configuration file. Figure 7 shows the total power demand in the region DolAmroth, as it is computed by plan4res out of the values in column value of ZV_ZoneValues.csv and the different timeseries in column Profile_Timeseries.

Figure 7: Power demand scenarios in region DolAmroth

This file contains the description of the network, ie the set of **lines** connecting the different **nodes**. (remind that the nodes are described in the first column of ZP_ZonePartition.csv).

Table 7: IN_Interconnectionscsv

| 011DolAmroth>Harad11DolAmroth11Harad117111-10011RoGonDor>DolAmroth11RoGonDor11DolAmroth11220011-200011RoGonDor>Harad11RoGonDor11Harad1186611-1160 |

|---|

|  |  |  |

|  |

In_Interconnections.csv may contain the following columns (optional columns are highlighted): (*Note that all numerical values may be replaced by the name of a deterministic Timeserie*):

- **Name**: name of the line (used for processing results)

- **StartLine** and **EndLine** must be nodes defined in the first column of ZP_ZonePartition.csv.

- **MaxPowerFlow** and **MinPowerFlow** are the bounds in MW on the flows for this line (one way or the other); *MaxPowerFlow* is the maximal flow from Start to End, while *MinPowerFlow* (which can be negative) is the minimum flow from Start to End. *(-1)*MinPowerFlow* is also the maximum flow between End and Start while *(-1)*MaxPowerFlow* is the minimum flow between Start and End.

- **Impedance** (optional, default 0): Impedance of the line

- **Cost** (optional, default 0): Cost of the line in €/MWh

These data files allow to describe the different kinds of generation units. It also allows to describe some load control mechanisms, such as load shifting, or management of electric vehicle charging.

This files gives the characteristics of all thermal power plants (and of all the power plants which are modelled as thermal power plants in plan4res, such as Geothermal plants).

Table 8: TU_ThermalUnits.csv

| 011RoGonDor11Biomass|w/o CCS1111119573.5113.81611011DolAmroth11Biomass|w/o CCS11111367.12113.81611011Harad11Biomass|w/o CCS11111469.141614113.81611011RoGonDor11Coal|Hard coal|w/o CCS1111116445.9549113110.751211DolAmroth11Coal|Hard coal|w/o CCS1111111.923392113110.751211Harad11Coal|Hard coal|w/o CCS111111783.37195113110.751211RoGonDor11Coal|Lignite|w/o CCS111115339.78409113110.9497142911RoGonDor11Gas|CCGT|w/o CCS1111183694.00231181.6648775110.3463448311DolAmroth11Gas|CCGT|w/o CCS1111120001182.0429943110.3463448311Harad11Gas|CCGT|w/o CCS11111150001181.517916110.3463448311RoGonDor11Gas|OCGT|w/o CCS111112200011113.409441110.5286315811Harad11Gas|OCGT|w/o CCS111112500011113.205328110.5286315811RoGonDor11Nuclear1111150783.183111811011DolAmroth11Nuclear11111500011811011Harad11Nuclear111114000011811011RoGonDor11Oil|w/o CCS111118652.37627110.036110.7010526311Harad11Oil|w/o CCS111113.94960304110.036110.70105263 |

|---|

|  |  |  |

|  |

It contains the following data (*Note that some of the numerical values may be replaced by the name of a deterministic Timeserie.* In that case the timeseries must be present in the Deterministic timeseries CSV file (see ):

- **Name**: name of the technology, or name of the plant. The list of names must be present in the settingsCreateInputPlan4res_*xxx*.yml configuration file (technos section, thermal), as this list is used in particular for post-treatments of results. Whenever the user wishes to add a new technology or plant, it must be added to the list in the settingsCreateInputPlan4res_*xxx*.yml configuration file.

- **Zone**: the values in this column must be included in the list of **nodes**, which is given in the first column of ZP_ZonePartition.csv, and corresponds to the lowest granularity of regions.

- **NumberUnits**: number of units of the given characteristics.

- **MaxPower**: maximum power of a single unit in MW. When NumberUnits=1, MaxPower is equal to Capacity.

- **Profile_Timeserie** (optional): deterministic or stochastic timeseries which will be applied to MaxPower. This allows accounting for eg. Maintenances and outages.

- **MinPower** (optional, 0 by default)Note that data consistency is ensured: if MinPower > MaxPower at some point, then MinPower = MaxPower. For example, this is useful if MaxPower = 0 during a period to model a maintenance or an outage. For thermal units, MinPower constraint applies only if the unit is started. : minimum power of a single unit in MW. Can be a deterministic timeseries. *This constraint is relaxed in SSV and CEM, as well as in SIM when the user requires to use continuous relaxation (see parameter in SMS++ configuration files)*

- **Pauxiliary** (optional, 0 by default): Power (MW) taken from the system when off for each unit. Can be a deterministic timeseries. *This constraint is relaxed in SSV and CEM, as well as in SIM when the user requires to use continuous relaxation (see parameter in SMS++ configuration files)*

- **VariableCost** (optional, 0 by default): proportional cost in €/MWh. Can be a deterministic timeseries.

- **FixedCost** (optional, 0 by default): fixed cost in €. Can be a deterministic timeseries.

- **Quadterm** (optional, 0 by default): quadratic cost. Can be a deterministic timeseries.

- **StartUpCost** (optional, 0 by default): cost (€) for starting the unit after a shut down. Can be a deterministic timeseries. *This constraint is relaxed in SSV and CEM, as well as in SIM when the user requires to use continuous relaxation (see parameter in SMS++ configuration files)*

- **MinUpTime** (optional, 1 hour by default): minimum duration when the plant is on (number of hours). *This constraint is relaxed in SSV and CEM, as well as in SIM when the user requires to use continuous relaxation (see parameter in SMS++ configuration files)*

- **MinDownTime** (optional, 1 hour by default): minimum duration when the plant is off (number of hours). *This constraint is relaxed in SSV and CEM, as well as in SIM when the user requires to use continuous relaxation (see parameter in SMS++ configuration files)*

- **Inertia** (optional, 0 by default): maximum inertia that can be provided by a unit in MWs/MWA. Can be a deterministic timeseries.

- **PrimaryRho** (optional, 0 by default): this parameter, multiplied by Maxpower, gives the maximum share of the active power that can be used as primary reserve. Can be a deterministic timeseries.

- **SecondaryRho** (optional, 0 by default): this parameter, multiplied by MaxPower, gives the maximum share of the active power that can be used as secondary reserve (optional, 0 by default). Can be a deterministic timeseries.

- **DeltaRampDown** (optional, MaxPower by default): maximum gradient when the power is decreased from one time step to the other, MW per hour. Can be a deterministic timeseries. *This constraint is relaxed in SSV and CEM, as well as in SIM when the user requires to use continuous relaxation (see parameter in SMS++ configuration files)*

- **DeltaRampUp** (optional, Maxpower by default): maximum gradient when the power is increased from one time step to the other, MW per hour. Can be a deterministic timeseries. *This constraint is relaxed in SSV and CEM, as well as in SIM when the user requires to use continuous relaxation (see parameter in SMS++ configuration files)*

- **CO2** (optional, 0 by default): emission rate in tons CO2 per MWh

- **Any other pollutant** which is defined in the coupling constraints section of the settingsCreateInputPlan4res_*xxx*.yml configuration file.

This file gives the characteristics of all seasonal storages. Only aggregated seasonal storages (ie one with one reservoir) can be described in this file (although SMS++ is capable of handling complex hydrovalleys).

Table 9: SS_SeasonalStorage.csv

| 011Hydro|Reservoir11RoGonDor1101111125814.051101151628100110117.5E+0711Inflows_RoGonDor.csv1134418733.311111011Hydro|Reservoir11DolAmroth110111115524.23941101111048478.9110111.6E+0711Inflow_DolAmroth.csv116629087.3311111011Hydro|Reservoir11Harad1101111160001101112000000110112.8E+0711Inflow_Harad.csv116000000111110 |

|---|

|  |  |  |

|  |

It contains the following columns (*Note that all numerical values may be replaced by the name of a deterministic Timeserie*):

- **Name**: name of the technology, or name of the plant. The list of names must be present in the settingsCreateInputPlan4res_*xxx*.yml configuration file (technos section, reservoir), as this list is used in particular for post-treatments of results. Whenever the user wishes to add a new technology or plant, it must be added to the list in the settingsCreateInputPlan4res_*xxx*.yml configuration file.

- **Zone**: the values in this column must be included in the list of **nodes**, which is given in the first column of ZP_ZonePartition.csv, and corresponds to the lowest granularity of regions.

- **NumberUnits**: number of units of the same type at the same location.

- **MaxPower** : maximum power of a single unit in MW. When NumberUnits=1, MaxPower is equal to Capacity. Can be a deterministic timeserie.

- **MinPower**As in ThermalUnits, consistency between MinPower and MaxPower is ensured such that Minpower can never be greater than MaxPower. (optional, 0 by default) Note that for hydro storages, MinPower forces the plant to run: it aims at representing hydro operational constraints such as minimal river flows. It is different from the MinPower constraint applied to thermal units. : minimum power of a single unit in MW. Can be a deterministic timeseries. *This constraint is relaxed in SSV and CEM, as well as in SIM when the user requires to use continuous relaxation (see parameter in SMS++ configuration files)*

- **DeltaRampDown** (optional, MaxPower by default): maximum gradient when the power is decreased from one time step to the other, MW per hour. Can be a deterministic timeseries. *This constraint is relaxed in SSV and CEM, as well as in SIM when the user requires to use continuous relaxation (see parameter in SMS++ configuration files)*

- **DeltaRampUp** (optional, Maxpower by default): maximum gradient when the power is increased from one time step to the other, MW per hour. Can be a deterministic timeseries. *This constraint is relaxed in SSV and CEM, as well as in SIM when the user requires to use continuous relaxation (see parameter in SMS++ configuration files)*

- **MaxVolume** : maximum volume of the reservoir (MWh). Can be a deterministic timeseries.

- **MinVolume**Consistency between MinVolume and MaxVolume is ensured, such that MinVolume can never be greater than MaxVolume. (optional, 0 by default) : minimum volume of the reservoir (MWh). Can be a deterministic timeseries.

- **TurbineEfficiency**: (optional, 1 by default). This value, multiplied by the flow, gives the generated power.

- **PumpingEfficiency**: (optional, 1 by default, but should be lower than TurbineEfficiency in practice). This value, multiplied by the flow, gives the generated power.

- **Inflows**: (optional, 0 by default; mandatory if column InflowsProfile is present). Inflows to the upstream reservoir (energy per year in MWh).

- **InflowsProfile**: (optional): time series profile for Inflows. Multiplied by the Inflows in energy, gives the inflows time series. These timeseries may be stochastic (in that case the value has to be XXX.csv), or deterministic.

- **InitialVolume**: (optional, 0 by default). Initial Volume of the upstream reservoir (MWh)

- **Inertia** (optional, 0 by default): maximum inertia that can be provided by a unit in MWs/MWA. Can be a deterministic timeseries.

- **PrimaryRho**: (%) this parameter, multiplied by MaxPower, gives the maximum primary reserve that can be provided by a unit (optional, 0 by default). Can be a deterministic timeserie.

- **SecondaryRho**: (%) this parameter, multiplied by MaxPower, gives the maximum secondary reserve that can be provided by a unit (optional, 0 by default). Can be a deterministic timeserie.

- **WaterValues**: optional; used to specify water values as input data from a file, if they are/were not computed by the current run (for example, coming from a previous SSV run). Contains the name of the file/sheet where the water values are stored. When using the simulation mode with one Bellman values (BV) file for all units (ie a polyhedral function), this file is only given in the first line; when using the simulation mode with 1 BV per unit (ie one function per reservoir), this file is given at each line; in optimization mode (= when running the SSV), this is not used as computed by the model. This column is always optional as the BV file (in case it is a polyhedral function) can be passed to SMS++ when calling the solver.

This file is used for:

- Pumped hydro

- Batteries

- Other flexibilities such as residential flexibilities (in particular load shifting) or electric vehicles (EV), which are modelled as short-term storages.

Table 10: STS_ShortTermStorage.csv

| 011Hydro|Pumped Storage11RoGonDor1111112150.5411-12150.54111215054110110.866110.86611Hydro|Pumped Storage11DolAmroth11111330211-330211330200110110.866110.86611Hydro|Pumped Storage11Harad111115920.7211-5920.7211592072110110.866110.86611Battery|Lithium-Ion11RoGonDor11111142775.46611-14275.4711571101.864110110.95110.9511Battery|Lithium-Ion11DolAmroth111113915.3490911-391.34911115661.3964110110.95110.9511Battery|Lithium-Ion11Harad1111127246.119311-27246.11911108984.477110110.95110.95 |

|---|

|  |  |  |

|  |

This file contains the following data:

- **Name**: name of the technology, or name of the plant. The list of names must be present in the settingsCreateInputPlan4res_*xxx*.yml configuration file, as this list is used in particular for post-treatments of results. Whenever the user wishes to add a new technology or plant, it must be added to the list in the settingsCreateInputPlan4res_*xxx*.yml configuration file.

- **Zone**: the values in this column must be included in the list of **nodes**, which is given in the first column of ZP_ZonePartition.csv, and corresponds to the lowest granularity of regions.

- **NumberUnits**: number of units of the same type at the same location.

- **MaxPower**: maximum power of a single unit in MW. When NumberUnits=1, MaxPower is equal to Capacity.

- **MaxPowerProfile** (optional): deterministic timeseries, which will be multiplied by MaxPower to obtain the MaxPower timeseries in MW.

- **MinPower** (optional, 0 by default) Note that for hydro storages, MinPower forces the plant to run: it aims at representing hydro operational constraints such as minimal river flows. It is different from the MinPower constraint applied to thermal units. Consistency between MinPower and MaxPower is ensured, MinPower can never be greater than MaxPower.: minimum power of a single unit in MW. Can be a deterministic timeserie. *This constraint is relaxed in SSV and CEM, as well as in SIM when the user requires to use continuous relaxation (see parameter in SMS++ configuration files)*

- **MaxVolume**Consistency between MinVolume and MaxVolume is ensured. MinVolume can never be greater than MaxVolume: maximum volume of the reservoir (MWh)..

- **MaxStorageProfile** (optional): deterministic timeseries, which will be multiplied by MaxVolume to obtain the MaxVolume timeserie in MWh.

- **MinVolume** (optional, 0 by default): minimum volume of the reservoir (MWh). Can be a deterministic timeserie.

- **TurbineEfficiency** (optional, 1 by default): This value, multiplied by the flow, gives the generated power. Can be a deterministic timeserie.

- **PumpingEfficiency** (optional, 1 by default, but should be lower than TurbineEfficiency in practice): This value, multiplied by the flow, gives the generated power. Can be a deterministic timeserie.

- **Inflows** (optional, 0 by default):

- **InitialPower** (optional, 0 by default): Initial Power of the unit (MW)

- **InitialStorage** (optional, 0 by default): Initial Volume of the upstream reservoir (MWh)

- **Inertia** (optional, 0 by default): maximum inertia that can be provided by a unit in MWs/MWA. Can be a deterministic timeserie.

- **MaxPrimaryPower** (optional, 0 by default): maximum primary reserve that can be provided by a unit. Can be a deterministic timeserie.

- **MaxSecondaryPower** (optional, 0 by default): maximum secondary reserve that can be provided by a unit (optional, 0 by default). Can be a deterministic timeserie.

- **DeltaRampDown** (optional, MaxPower by default): maximum gradient when the power is decreased from one time step to the other, MW per hour. Can be a deterministic timeseries. *This constraint is relaxed in SSV and CEM, as well as in SIM when the user requires to use continuous relaxation (see parameter in SMS++ configuration files)*

- **DeltaRampUp** (optional, Maxpower by default): maximum gradient when the power is increased from one time step to the other, MW per hour. Can be a deterministic timeseries. *This constraint is relaxed in SSV and CEM, as well as in SIM when the user requires to use continuous relaxation (see parameter in SMS++ configuration files)*

- **Cost** (optional, 0 by default): proportional cost (€/MWh). Can be a deterministic timeseries.

- **Inflows**: (optional, 0 by default). Inflows to the upstream reservoir (MWh). If negative it is considered to be a consumption linked to the unit (eg consumption of EV). Can be a deterministic timeseries.

- **VolumeLevelTarget**If an InitialStorage is not provided, VolumeLevelTarget will be used as InitialStorage.: (optional) used to force the optimization to reach this volume at the end of each stage. If there is a VolumeLevelTarget, the minimum volume constraint is replaced by this value at the first and last time-steps of each stage.

This file gives the characteristics of the variable renewable units: windpower, PV power and run-of-river units.

Table 11: RES_RenewableUnits.csv

| 011Wind|Onshore11DolAmroth111119923.3311011ONSHORE_OPT_DolAmroth.csv11Wind|Offshore11RoGonDor1111118113.3311011Offshore-Deep_RoGonDor.csv |

|---|

|  |  |  |

|  |

It contains the following data:

- **Name**: name of the technology, or name of the plant. The list of names must be present in the settingsCreateInputPlan4res_*xxx*.yml configuration file (technos section, thermal), as this list is used in particular for post-treatments of results. Whenever the user wishes to add a new technology or plant, it must be added to the list in the settingsCreateInputPlan4res_*xxx*.yml configuration file.

- **Zone**: the values in this column must be included in the list of **nodes**, which is given in the first column of ZP_ZonePartition.csv, and corresponds to the lowest granularity of regions.

- **NumberUnits**: number of units of the same type at the same location.

- **MaxPower**: capacity for PV and WindPower; yearly average energy for run-of-river) – This is due to the fact that the available load factor timeseries for Wind and PV Power and for run-of-river were computed with different methods. The maximum potential production for Wind or PV is equal to the capacity multiplied by the load factor timeseries while the maximum potential production for a run-of-river is equal to the average yearly energy multiplied by the timeseries.)

- maximum power of a single unit in MW. When NumberUnits=1, MaxPower is equal to Capacity.

- **MaxPowerProfile** (optional): deterministic or stochastic timeseries which will be applied to MaxPower. This allows accounting for in particular the variability of the potential power, given its correlation with climate variables (sun, wind…).

- **MinPower** (optional, 0 by default)Note that data consistency is ensured: if MinPower > MaxPower at some point, then MinPower = MaxPower. For example, this is useful if MaxPower = 0 during a period to model a maintenance or an outage. For thermal units, MinPower constraint applies only if the unit is started. : minimum power of a single unit in MW. Can be a deterministic timeseries. *This constraint is relaxed in SSV and CEM, as well as in SIM when the user requires to use continuous relaxation (see parameter in SMS++ configuration files)*

- **Inertia** (optional, 0 by default): maximum inertia that can be provided by a unit in MWs/MWA. Can be a deterministic timeserie.

- **Gamma** (optional, 1 by default): this parameter is used by the model to determine the maximum available primary and secondary reserve. In practice, the model accounts for the following constraint: at each timestep, the sum of the primary and secondary reserves is lower than the maximum power minus the generated power.

To run the Capacity Expansion Model (CEM), 4 columns need to be added to the files corresponding to assets in which one wants to invest (see below), ie to the files describing the generation units (apart from Seasonal Storages) as well as to the file describing the interconnection (see ):

Table 12: additional columns for capacity expansion

| 011DolAmroth11Biomass|w/o CCS111119800001110011500011011RoGonDor11Biomass|w/o CCS111119800001110011400011011Harad11Biomass|w/o CCS11111980000111001150011011DolAmroth11Coal|Hard coal|w/o CCS1111108225011100110112000 |

|---|

|  |  |  |

|  |

- **MaxAddedCapacity**: this is the maximum capacity that may be added, in MW.

- **MaxRetCapacity**: this is the maximum capacity that may be decommissioned, in MW.

- **InvestmentCost**: this is the cost for investing into the given capacity in the given zone, in €/MW. Note that these are yearly costs, computed as Capital Cost / LifeTime (in years) + Fixed Cost.

- **DecommissionCost**: this is the cost for decommissioning the given capacity in the given zone, in €/MW.

Costs are not discounted.

These columns may then be added to the following files:

- IN_Interconnections.csv

- TU_ThermalUnits.csv

- STS_ShortTermStorage.csv

- RES_RenewableUnits.csv

Note that investment in new seasonal storages is not available at present.