### Geography and coupling constraints : files ZP_ZonePartition, ZV_ZoneValues, IN_Interconnections

This first group of data files is used to describe the regions in the
dataset, the interconnections between the regions, and the constraints
at region level, such as the power demand, but also the system services.

#### File ZP_ZonePartition.csv

The file ZP_ZonePartition.csv describes the different regions that are
used in the dataset. In the example below, the lower level (on the left)
corresponds to countries.

The lower level is used to define **Nodes**. Each generation unit
(defined in TU_ThermalUnits.csv, RES_RenewableUnits.csv,
STS_ShortTermUnits.csv and SS_SeasonalStorage.csv) belongs to one
**Node**. Interconnections (defined in IN_Interconnections.csv) are
connecting nodes.

The higher level corresponds to continents (with a unique continent
called 'MiddleEarth'). There could exist intermediate levels. The
different levels are used to define "coupling constraints" (see
***Erreur ! Source du renvoi introuvable.** **Erreur ! Source du renvoi
introuvable.***), such as the power demand which is always linked to a
Node. Other coupling constraints (such as system services) may apply to
different levels. (See ***Erreur ! Source du renvoi introuvable.**
**Erreur ! Source du renvoi introuvable.*** for more details about
regions)

Table 4: ZP_ZonePartition.csv

  -----------------------------------------------------------------------
  **Countries**                     **Continent**
  --------------------------------- -------------------------------------
  RoGonDor                          MiddleEarth

  DolAmroth                         MiddleEarth

  Harad                             MiddleEarth
  -----------------------------------------------------------------------

The different regions can be defined by the user in the
settingsCreateInputPlan4res\_*xxx*.yml configuration file (Regions
section).

#### File ZV_ZoneValues.csv 

This file contains the values of all coupling constraints (in particular
the demand at each Node, which is mandatory). It may also optionally
contain the parameters for defining the costs associated to imbalance
(for each coupling constraint). These parameters can also be defined in
the settingsCreateInputPlan4res\_*xxx*.yml configuration file (Coupling
constraints section), in particular if the user wishes to use the same
parameters for all the regions. If the user wishes to use different
values, they must appear in ZV_ZoneValues.csv.

Table 5: ZV_ZoneValues.csv

  ---------------------------------------------------------------------------------------
  **Type**                     **Zone**    **Value**     **Profile_Timeserie**
  ---------------------------- ----------- ------------- --------------------------------
  Cooking                      DolAmroth   7178950.652   TS_COOKING_DolAmroth.csv

  ElecHeating                  DolAmroth   54635950.13   TS_HEAT_LOW_DolAmroth.csv

  ElecVehicle                  DolAmroth   13541851.26   TS_MOBILITY_PSNG_DolAmroth.csv

  OtherExclHeatTranspCooking   DolAmroth   51369219.81   TS_LOAD_DolAmroth.csv

  CostActivePowerDemand        DolAmroth   10000         

  MaxActivePowerDemand         DolAmroth   1500000       
  ---------------------------------------------------------------------------------------

Table 5 shows the content of ZV_ZoneValues.csv for the region
"DolAmroth". In this example, tere is only one type of coupling
constraint per region, which is the power demand. The power demand is
composed of 4 parts: power demand for cooking, for heating
(ElecHeating), for transportation (ElecVehicle) and for other uses
(OtherExclHeatTranspCooking). The unit of the values in the column
'value' is MWh or €/MWh (for the variables of Type Cost\*). The row
'Cooking' gives in column 'value' the power demand for cooking in the
region DolAmroth for the year, in MWh, as well as the name of the
timeseries to use to compute the hourly power demand for cooking (here
TS_COOKING_DolAmroth.csv). Whenever the timserie would be deterministic,
the Profile_Timeserie column would contain the name of the column
corresponding to this timeseries in the csv file containing all
deterministic timeseries. Table 6 shows the first 6 hours of this
timeseries, for the 3 scenarios 'Base', 'PVminus10' and 'Demandplus10').
The (here scenarized) hourly power demand for cooking is computed by
multiplying the timeseries by the numerical value in ZV_ZoneValue.csv.

Table 6: TS_COOKING_DolAmroth.csv

  ---------------------------------------------------------------------------
  **Timestamp \[UTC\]**      **Base**      **PVminus10**   **Demandplus10**
  -------------------------- ------------- --------------- ------------------
  01/01/2050 00:00           1.60E-05      1.60E-05        1.76E-05

  01/01/2050 01:00           1.60E-05      1.60E-05        1.76E-05

  01/01/2050 02:00           1.60E-05      1.60E-05        1.76E-05

  01/01/2050 03:00           1.60E-05      1.60E-05        1.76E-05

  01/01/2050 04:00           1.60E-05      1.60E-05        1.76E-05

  01/01/2050 05:00           1.60E-05      1.60E-05        1.76E-05

  01/01/2050 06:00           3.31E-05      3.31E-05        3.64E-05
  ---------------------------------------------------------------------------

The total power demand (scenarized) timeseries of the region is computed
by adding the 4 timeseries corresponding to the 4 parts of the power
demand. The way of computing the power demand is defined in the
settingsCreateInputPlan4res\_*xxx*.yml configuration file. Figure 7
shows the total power demand in the region DolAmroth, as it is computed
by plan4res out of the values in column value of ZV_ZoneValues.csv and
the different timeseries in column Profile_Timeseries.

Figure 7: Power demand scenarios in region DolAmroth

#### File IN_Interconnections.csv

This file contains the description of the network, ie the set of
**lines** connecting the different **nodes**. (remind that the nodes are
described in the first column of ZP_ZonePartition.csv).

Table 7: IN_Interconnectionscsv

  -----------------------------------------------------------------------------------------
  **Name**              **StartLine**   **EndLine**   **MaxPowerFlow**   **MinPowerFlow**
  --------------------- --------------- ------------- ------------------ ------------------
  DolAmroth\>Harad      DolAmroth       Harad         71                 -100

  RoGonDor\>DolAmroth   RoGonDor        DolAmroth     2200               -2000

  RoGonDor\>Harad       RoGonDor        Harad         866                -1160
  -----------------------------------------------------------------------------------------

In_Interconnections.csv may contain the following columns (optional
columns are highlighted): (*Note that all numerical values may be
replaced by the name of a deterministic Timeserie*):

-   **Name**: name of the line (used for processing results)

-   **StartLine** and **EndLine** must be nodes defined in the first
    column of ZP_ZonePartition.csv.

-   **MaxPowerFlow** and **MinPowerFlow** are the bounds in MW on the
    flows for this line (one way or the other); *MaxPowerFlow* is the
    maximal flow from Start to End, while *MinPowerFlow* (which can be
    negative) is the minimum flow from Start to End.
    *(-1)\*MinPowerFlow* is also the maximum flow between End and Start
    while *(-1)\*MaxPowerFlow* is the minimum flow between Start and
    End.

-   **Impedance** (optional, default 0): Impedance of the line

-   **Cost** (optional, default 0): Cost of the line in €/MWh

