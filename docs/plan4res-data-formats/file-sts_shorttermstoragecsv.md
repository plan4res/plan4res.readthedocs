### File STS_ShortTermStorage.csv

This file is used for:

-   Pumped hydro

-   Batteries

-   Other flexibilities such as residential flexibilities (in particular
    load shifting) or electric vehicles (EV), which are modelled as
    short-term storages.

Table 10: STS_ShortTermStorage.csv

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Name**               **Zone**    **NumberUnits**   **MaxPower**   **MinPower**   **MaxVolume**   **MinVolume**   **TurbineEfficiency**   **PumpingEfficiency**
  ---------------------- ----------- ----------------- -------------- -------------- --------------- --------------- ----------------------- -----------------------
  Hydro\|Pumped Storage  RoGonDor    1                 12150.54       -12150.54      1215054         0               0.866                   0.866

  Hydro\|Pumped Storage  DolAmroth   1                 3302           -3302          330200          0               0.866                   0.866

  Hydro\|Pumped Storage  Harad       1                 5920.72        -5920.72       592072          0               0.866                   0.866

  Battery\|Lithium-Ion   RoGonDor    1                 142775.466     -14275.47      571101.864      0               0.95                    0.95

  Battery\|Lithium-Ion   DolAmroth   1                 3915.34909     -391.3491      15661.3964      0               0.95                    0.95

  Battery\|Lithium-Ion   Harad       1                 27246.1193     -27246.119     108984.477      0               0.95                    0.95
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------

This file contains the following data:

-   **Name**: name of the technology, or name of the plant. The list of
    > names must be present in the
    > settingsCreateInputPlan4res\_*xxx*.yml configuration file, as this
    > list is used in particular for post-treatments of results.
    > Whenever the user wishes to add a new technology or plant, it must
    > be added to the list in the settingsCreateInputPlan4res\_*xxx*.yml
    > configuration file.

-   **Zone**: the values in this column must be included in the list of
    > **nodes**, which is given in the first column of
    > ZP_ZonePartition.csv, and corresponds to the lowest granularity of
    > regions.

-   **NumberUnits**: number of units of the same type at the same
    > location.

-   **MaxPower**: maximum power of a single unit in MW. When
    > NumberUnits=1, MaxPower is equal to Capacity.

-   **MaxPowerProfile** (optional): deterministic timeseries, which will
    > be multiplied by MaxPower to obtain the MaxPower timeseries in MW.

-   **MinPower** (optional, 0 by default) [^28] [^29]: minimum power of
    > a single unit in MW. Can be a deterministic timeserie. *This
    > constraint is relaxed in SSV and CEM, as well as in SIM when the
    > user requires to use continuous relaxation (see parameter in SMS++
    > configuration files)*

-   **MaxVolume**[^30]: maximum volume of the reservoir (MWh)..

-   **MaxStorageProfile** (optional): deterministic timeseries, which
    > will be multiplied by MaxVolume to obtain the MaxVolume timeserie
    > in MWh.

-   **MinVolume** (optional, 0 by default): minimum volume of the
    > reservoir (MWh). Can be a deterministic timeserie.

-   **TurbineEfficiency** (optional, 1 by default): This value,
    > multiplied by the flow, gives the generated power. Can be a
    > deterministic timeserie.

-   **PumpingEfficiency** (optional, 1 by default, but should be lower
    > than TurbineEfficiency in practice): This value, multiplied by the
    > flow, gives the generated power. Can be a deterministic timeserie.

-   **Inflows** (optional, 0 by default):

-   **InitialPower** (optional, 0 by default): Initial Power of the unit
    > (MW)

-   **InitialStorage** (optional, 0 by default): Initial Volume of the
    > upstream reservoir (MWh)

-   **Inertia** (optional, 0 by default): maximum inertia that can be
    > provided by a unit in MWs/MWA. Can be a deterministic timeserie.

-   **MaxPrimaryPower** (optional, 0 by default): maximum primary
    > reserve that can be provided by a unit. Can be a deterministic
    > timeserie.

-   **MaxSecondaryPower** (optional, 0 by default): maximum secondary
    > reserve that can be provided by a unit (optional, 0 by default).
    > Can be a deterministic timeserie.

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

-   **Cost** (optional, 0 by default): proportional cost (€/MWh). Can be
    > a deterministic timeseries.

-   **Inflows**: (optional, 0 by default). Inflows to the upstream
    > reservoir (MWh). If negative it is considered to be a consumption
    > linked to the unit (eg consumption of EV). Can be a deterministic
    > timeseries.

-   **VolumeLevelTarget**[^31]: (optional) used to force the
    > optimization to reach this volume at the end of each stage. If
    > there is a VolumeLevelTarget, the minimum volume constraint is
    > replaced by this value at the first and last time-steps of each
    > stage.

#### File RES_RenewableUnits.csv

This file gives the characteristics of the variable renewable units:
windpower, PV power and run-of-river units.

Table 11: RES_RenewableUnits.csv

  ---------------------------------------------------------------------------------------------------------
  **Name**         **Zone**    **NumberUnits**   **MaxPower**   **MinPower**   **MaxPowerProfile**
  ---------------- ----------- ----------------- -------------- -------------- ----------------------------
  Wind\|Onshore    DolAmroth   1                 9923.33        0              ONSHORE_OPT_DolAmroth.csv

  Wind\|Offshore   RoGonDor    1                 18113.33       0              Offshore-Deep_RoGonDor.csv
  ---------------------------------------------------------------------------------------------------------

It contains the following data:

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

-   **NumberUnits**: number of units of the same type at the same
    > location.

-   **MaxPower**: capacity for PV and WindPower; yearly average energy
    > for run-of-river) -- This is due to the fact that the available
    > load factor timeseries for Wind and PV Power and for run-of-river
    > were computed with different methods. The maximum potential
    > production for Wind or PV is equal to the capacity multiplied by
    > the load factor timeseries while the maximum potential production
    > for a run-of-river is equal to the average yearly energy
    > multiplied by the timeseries.)

-   maximum power of a single unit in MW. When NumberUnits=1, MaxPower
    > is equal to Capacity.

-   **MaxPowerProfile** (optional): deterministic or stochastic
    > timeseries which will be applied to MaxPower. This allows
    > accounting for in particular the variability of the potential
    > power, given its correlation with climate variables (sun,
    > wind...).

-   **MinPower** (optional, 0 by default)[^32] : minimum power of a
    > single unit in MW. Can be a deterministic timeseries. *This
    > constraint is relaxed in SSV and CEM, as well as in SIM when the
    > user requires to use continuous relaxation (see parameter in SMS++
    > configuration files)*

-   **Inertia** (optional, 0 by default): maximum inertia that can be
    > provided by a unit in MWs/MWA. Can be a deterministic timeserie.

-   **Gamma** (optional, 1 by default): this parameter is used by the
    > model to determine the maximum available primary and secondary
    > reserve. In practice, the model accounts for the following
    > constraint: at each timestep, the sum of the primary and secondary
    > reserves is lower than the maximum power minus the generated
    > power.

