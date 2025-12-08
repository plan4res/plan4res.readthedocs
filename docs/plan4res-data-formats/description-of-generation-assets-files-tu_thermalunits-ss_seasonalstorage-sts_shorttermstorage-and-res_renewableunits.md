### Description of generation assets : files TU_ThermalUnits, SS_SeasonalStorage, STS_ShortTermStorage and RES_RenewableUnits

These data files allow to describe the different kinds of generation
units. It also allows to describe some load control mechanisms, such as
load shifting, or management of electric vehicle charging.

#### File TU_ThermalUnits.csv

This files gives the characteristics of all thermal power plants (and of
all the power plants which are modelled as thermal power plants in
plan4res, such as Geothermal plants).

Table 8: TU_ThermalUnits.csv

  --------------------------------------------------------------------------------------------------
  **Zone**    **Name**             **NumberUnits**   **MaxPower**   **VariableCost**   **CO2Rate**
  ----------- -------------------- ----------------- -------------- ------------------ -------------
  RoGonDor    Biomass\|w/o CCS     1                 19573.5        3.816              0

  DolAmroth   Biomass\|w/o CCS     1                 367.12         3.816              0

  Harad       Biomass\|w/o CCS     1                 469.141614     3.816              0

  RoGonDor    Coal\|Hard coal\|w/o 1                 16445.9549     3                  0.7512
              CCS                                                                      

  DolAmroth   Coal\|Hard coal\|w/o 1                 11.923392      3                  0.7512
              CCS                                                                      

  Harad       Coal\|Hard coal\|w/o 1                 1783.37195     3                  0.7512
              CCS                                                                      

  RoGonDor    Coal\|Lignite\|w/o   1                 5339.78409     3                  0.94971429
              CCS                                                                      

  RoGonDor    Gas\|CCGT\|w/o CCS   1                 83694.0023     81.6648775         0.34634483

  DolAmroth   Gas\|CCGT\|w/o CCS   1                 2000           82.0429943         0.34634483

  Harad       Gas\|CCGT\|w/o CCS   1                 15000          81.517916          0.34634483

  RoGonDor    Gas\|OCGT\|w/o CCS   1                 22000          113.409441         0.52863158

  Harad       Gas\|OCGT\|w/o CCS   1                 25000          113.205328         0.52863158

  RoGonDor    Nuclear              1                 50783.1831     8                  0

  DolAmroth   Nuclear              1                 5000           8                  0

  Harad       Nuclear              1                 40000          8                  0

  RoGonDor    Oil\|w/o CCS         1                 8652.37627     0.036              0.70105263

  Harad       Oil\|w/o CCS         1                 3.94960304     0.036              0.70105263
  --------------------------------------------------------------------------------------------------

It contains the following data (*Note that some of the numerical values
may be replaced by the name of a deterministic Timeserie.* In that case
the timeseries must be present in the Deterministic timeseries CSV file
(see ):

-   **Name**: name of the technology, or name of the plant. The list of
    > names must be present in the
    > settingsCreateInputPlan4res\_*xxx*.yml configuration file (technos
    > section, thermal), as this list is used in particular for
    > post-treatments of results. Whenever the user wishes to add a new
    > technology or plant, it must be added to the list in the
    > settingsCreateInputPlan4res\_*xxx*.yml configuration file.

-   **Zone**: the values in this column must be included in the list of
    > **nodes**, which is given in the first column of
    > ZP_ZonePartition.csv, and corresponds to the lowest granularity of
    > regions.

-   **NumberUnits**: number of units of the given characteristics.

-   **MaxPower**: maximum power of a single unit in MW. When
    > NumberUnits=1, MaxPower is equal to Capacity.

-   **Profile_Timeserie** (optional): deterministic or stochastic
    > timeseries which will be applied to MaxPower. This allows
    > accounting for eg. Maintenances and outages.

-   **MinPower** (optional, 0 by default)[^24] : minimum power of a
    > single unit in MW. Can be a deterministic timeseries. *This
    > constraint is relaxed in SSV and CEM, as well as in SIM when the
    > user requires to use continuous relaxation (see parameter in SMS++
    > configuration files)*

-   **Pauxiliary** (optional, 0 by default): Power (MW) taken from the
    > system when off for each unit. Can be a deterministic timeseries.
    > *This constraint is relaxed in SSV and CEM, as well as in SIM when
    > the user requires to use continuous relaxation (see parameter in
    > SMS++ configuration files)*

-   **VariableCost** (optional, 0 by default): proportional cost in
    > €/MWh. Can be a deterministic timeseries.

-   **FixedCost** (optional, 0 by default): fixed cost in €. Can be a
    > deterministic timeseries.

-   **Quadterm** (optional, 0 by default): quadratic cost. Can be a
    > deterministic timeseries.

-   **StartUpCost** (optional, 0 by default): cost (€) for starting the
    > unit after a shut down. Can be a deterministic timeseries. *This
    > constraint is relaxed in SSV and CEM, as well as in SIM when the
    > user requires to use continuous relaxation (see parameter in SMS++
    > configuration files)*

-   **MinUpTime** (optional, 1 hour by default): minimum duration when
    > the plant is on (number of hours). *This constraint is relaxed in
    > SSV and CEM, as well as in SIM when the user requires to use
    > continuous relaxation (see parameter in SMS++ configuration
    > files)*

-   **MinDownTime** (optional, 1 hour by default): minimum duration when
    > the plant is off (number of hours). *This constraint is relaxed in
    > SSV and CEM, as well as in SIM when the user requires to use
    > continuous relaxation (see parameter in SMS++ configuration
    > files)*

-   **Inertia** (optional, 0 by default): maximum inertia that can be
    > provided by a unit in MWs/MWA. Can be a deterministic timeseries.

-   **PrimaryRho** (optional, 0 by default): this parameter, multiplied
    > by Maxpower, gives the maximum share of the active power that can
    > be used as primary reserve. Can be a deterministic timeseries.

-   **SecondaryRho** (optional, 0 by default): this parameter,
    > multiplied by MaxPower, gives the maximum share of the active
    > power that can be used as secondary reserve (optional, 0 by
    > default). Can be a deterministic timeseries.

-   **DeltaRampDown** (optional, MaxPower by default): maximum gradient
    > when the power is decreased from one time step to the other, MW
    > per hour. Can be a deterministic timeseries. *This constraint is
    > relaxed in SSV and CEM, as well as in SIM when the user requires
    > to use continuous relaxation (see parameter in SMS++ configuration
    > files)*

-   **DeltaRampUp** (optional, Maxpower by default): maximum gradient
    > when the power is increased from one time step to the other, MW
    > per hour. Can be a deterministic timeseries. *This constraint is
    > relaxed in SSV and CEM, as well as in SIM when the user requires
    > to use continuous relaxation (see parameter in SMS++ configuration
    > files)*

-   **CO2** (optional, 0 by default): emission rate in tons CO2 per MWh

-   **Any other pollutant** which is defined in the coupling constraints
    > section of the settingsCreateInputPlan4res\_*xxx*.yml
    > configuration file.

