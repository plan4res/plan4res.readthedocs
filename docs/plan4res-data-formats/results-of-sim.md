### Results of SIM 

The simulation produces 2 sets of results:

-   Raw results of the simulation. They correspond to the outputs of the
    model, without any post-treatment (the post-treatment is performed
    when running POSTTREAT).

-   Post-treated results. These are results computed by the POSTTREAT
    function of plan4res.

#### Raw results of SIM

All row results follow the same format: the index column gives the
indexes of the simulation timesteps, while the other columns give the
values corresponding to the name in the header (which can be a region, a
technology....)

For each scenario \$i, the following files are produced.

-   Demand_Scen\$i_OUT.csv: 1 column per node with the power demand in
    the node.

-   ActivePower_Scen\$i_OUT.csv: generation schedules. 1 column per unit
    (apart from the Seasonal Storage units which are duplicated in 2
    columns: one for the generation part, and the other one for the
    pumping part). Note that all other units with storages comprise a
    unique column with both positive and negative (pumping) values.

-   Primary_Scen\$i_OUT.csv: primary reserve schedules. 1 column per
    unit (apart from the Seasonal Storage units which are duplicated in
    2 columns: one for the generation part, and the other one for the
    pumping part).

-   Secondary_Scen\$i_OUT.csv: secondary reserve schedules. 1 column per
    unit (apart from the Seasonal Storage units which are duplicated in
    2 columns: one for the generation part, and the other one for the
    pumping part)

-   Inertia_Scen\$i_OUT.csv : inertia provided by each unit. 1 column
    per unit (apart from the Seasonal Storage units which are duplicated
    in 2 columns: one for the generation part, and the other one for the
    pumping part).

-   Volume_Scen\$i_OUT.csv: volumes of each storage (seasonal storages
    and short-term storages).

-   Flows_Scen\$i_OUT.csv: flows between zones. 1 column per
    transmission line.

-   MarginalCostActivePowerDemand_Scen\$i_OUT.csv: marginal costs of the
    demand constraint. 1 column per node (ch the *ActivePowerDemand*
    constraint is always applied to Nodes).

-   MarginalCostPrimary_Scen\$i_OUT.csv: marginal costs of the primary
    reserve constraint. 1 column per region (at the partition level of
    the *PrimaryDemand* constraints, note that these constraints may
    apply to different regional partitions than the Demand. See section
    **Erreur ! Source du renvoi introuvable.**).

-   MarginalCostSecondary_Scen\$i_OUT.csv: marginal costs of the
    secondary reserve constraint. 1 column per zone (at the partition
    level of the *SecondaryDemand* constraints).

-   MarginalCostInertia_Scen\$i_OUT.csv: marginal costs of the Inertia
    constraint (at the partition level of the *InertiaDemand*
    constraints). 1 column per zone.

-   MarginalCostFlows_Scen\$i_OUT.csv: marginal costs of the lines. 1
    column per line.

-   MaxPower_Scen\$i_OUT.csv: maximum available power. 1 column per
    technology.

**All files share the same format: a header containing the names of the
series, an index with the time steps.**

#### Post-Treated resuls of SIM

##### Installed Capacity

***InstalledCapacity.csv and AggrInstalledCapacity.csv***: installed
capacities (aggregated installed capacity, with aggregations such as
defined in settingsPostTreatPlan4res.py) in the different available
technologies per zone. 1 column per technology, 1 row per node. (the
generation units are attached to nodes)

Table 14: InstalledCapacity.csv

  -------------------------------------------------------------------------------------------------------------
              **Hydro\|Reservoir**   **Biomass\|w/o   **Coal\|Hard    **Coal\|Lignite\|w/o   **Gas\|CCGT\|w/o
                                     CCS**            coal\|w/o CCS** CCS**                  CCS**
  ----------- ---------------------- ---------------- --------------- ---------------------- ------------------
  RoGonDor    25814.05               19573.5          16445.95488     5339.784093            83694.0023

  DolAmroth   5524.239444            367.12           11.923392       0                      2000

  Harad       6000                   469.1416144      1783.371951     0                      15000
  -------------------------------------------------------------------------------------------------------------

##### Generation

***Generation.csv and AggrGeneration.csv***: total average (on
scenarios) generation on the whole simulation time horizon (aggregated
generation, with aggregations such as defined in
settingsPostTreatPlan4res_XXX.py) from the different available
technologies per node. 1 column per technology, 1 row per node. Note
that the Non Served column corresponds to the non-served electricity.

Table 15: AggrGeneration.csv

  ---------------------------------------------------------------------------------
              **Hydro**    **WindPower**   **PV**       **Biomass**   **Nuclear**
  ----------- ------------ --------------- ------------ ------------- -------------
  RoGonDor    126850389    578839017       185813311    0             249852103

  DolAmroth   29932305.8   26161752.2      11697614.5   2944912.11    29463408.7

  Harad       37280301.6   10847753.5      117436876    4098421.14    346617336
  ---------------------------------------------------------------------------------

***Generation-NODE.csv*** and ***AggrGeneration-NODE.csv***: average
generation (aggregated generation) from the different available
technologies per node. 1 file per node, 1 column per technology, 1 row
per simulation time step.

Table 16: Generation-Harad.csv

+------------+----------------+----------------+----------------------+
|            | > Hy           | > Biomass\|w/o | > Coal\|Hard         |
|            | dro\|Reservoir | > CCS          | > coal\|w/o CCS      |
+============+================+================+======================+
| >          | > 886.9210309  | > 11259.39875  | > 42800.92681        |
| 02/07/2030 |                |                |                      |
+------------+----------------+----------------+----------------------+
| >          | > 0            | > 11259.39875  | > 42800.92681        |
| 03/07/2030 |                |                |                      |
+------------+----------------+----------------+----------------------+
| >          | > 0            | > 11259.39875  | > 42800.92681        |
| 04/07/2030 |                |                |                      |
+------------+----------------+----------------+----------------------+
| >          | > 0            | > 11259.39875  | > 42800.92681        |
| 05/07/2030 |                |                |                      |
+------------+----------------+----------------+----------------------+
| >          | > 0            | > 11259.39875  | > 42800.92681        |
| 06/07/2030 |                |                |                      |
+------------+----------------+----------------+----------------------+
| >          | > 0            | > 11259.39875  | > 42800.92681        |
| 07/07/2030 |                |                |                      |
+------------+----------------+----------------+----------------------+
| >          | > 0            | > 11259.39875  | > 42800.92681        |
| 08/07/2030 |                |                |                      |
+------------+----------------+----------------+----------------------+
| >          | > 19775.91482  | > 11259.39875  | > 42800.92681        |
| 09/07/2030 |                |                |                      |
+------------+----------------+----------------+----------------------+

***Generation-NODE-\$i.csv***: generation from the different available
technologies in the node for scenario \$i. 1 file per zone and scenario,
1 column per technology, 1 row per time step.

***Slack-ZONE.csv***: electricity not served per node. 1 file per node.
1 column per scenario, 1 row per time step.

Table 17: Slack-Harad.csv

  --------------------------------------------------------------------------
                 **Harad-0**    **Harad-1**    **Harad-2**    **Harad-3**
  -------------- -------------- -------------- -------------- --------------
  02/07/2030     0              0              0              0

  03/07/2030     0              0              0              0

  04/07/2030     0              0              0              0

  05/07/2030     0              0              0              0

  06/07/2030     0              0              0              0

  07/07/2030     0              0              0              0
  --------------------------------------------------------------------------

***nbHoursSlack.csv***: number of hours with non-served electricity per
node and scenario.

##### Costs

***MeanVariableCost.csv***: average variable costs. 1 column per node, 1
row per technology.

Table 18: MeanVariableCost.csv

+----------------------------+------------+-------------+-------------+
|                            | > **       | > **        | > **Harad** |
|                            | RoGonDor** | DolAmroth** |             |
+============================+============+=============+=============+
| > Hydro\|Reservoir         | > 0        | > 0         | > 0         |
+----------------------------+------------+-------------+-------------+
| > Biomass\|w/o CCS         | > 0        | >           | >           |
|                            |            |  11237784.6 |  15639575.1 |
+----------------------------+------------+-------------+-------------+
| > Coal\|Hard coal\|w/o CCS | >          | >           | >           |
|                            |  330248836 |  305191.142 |  46738612.1 |
+----------------------------+------------+-------------+-------------+
| > Coal\|Lignite\|w/o CCS   | >          | > 0         | > 0         |
|                            |  107785456 |             |             |
+----------------------------+------------+-------------+-------------+

***VariableCostPerScenario.csv***: variable costs. 1 column per scenario
and node, 1 row per techno.

Table 19: VariableCostPerScenario.csv

+-------------+----------+----------+----------+----------+----------+
|             | > **RoGo | > **RoGo | > **RoGo | > **RoGo | >        |
|             | nDor-0** | nDor-1** | nDor-2** | nDor-3** |  **DolAm |
|             |          |          |          |          | roth-0** |
+=============+==========+==========+==========+==========+==========+
| > Hydro     | > 0      | > 0      | > 0      | > 0      | > 0      |
| \|Reservoir |          |          |          |          |          |
+-------------+----------+----------+----------+----------+----------+
| > B         | > 0      | > 0      | > 0      | > 0      | > 11     |
| iomass\|w/o |          |          |          |          | 073780.1 |
| > CCS       |          |          |          |          |          |
+-------------+----------+----------+----------+----------+----------+

#### Marginal Costs

***meanScenCmar.csv***: average over all scenarios of the marginal
costs. 1 column par node, 1 row per time step.

Table 20: meanScenCmar.csv

+-----------------+----------------+----------------+-----------------+
|                 | > **RoGonDor** | >              | > **Harad**     |
|                 |                |  **DolAmroth** |                 |
+=================+================+================+=================+
| > 02/07/2030    | > 0.036        | > 8            | > 81.517916     |
+-----------------+----------------+----------------+-----------------+
| > 03/07/2030    | > 0.036        | > 7.415        | > 81.517916     |
+-----------------+----------------+----------------+-----------------+
| > 04/07/2030    | > 0.036        | > 8            | > 81.517916     |
+-----------------+----------------+----------------+-----------------+
| > 05/07/2030    | > 0.036        | > 5.999648     | > 81.517916     |
+-----------------+----------------+----------------+-----------------+
| > 06/07/2030    | > 0.036        | > 5.999648     | > 81.517916     |
+-----------------+----------------+----------------+-----------------+
| > 07/07/2030    | > 0.036        | > 5.999648     | > 77.5439176    |
+-----------------+----------------+----------------+-----------------+
| > 08/07/2030    | > 0.036        | > 5.999648     | > 81.517916     |
+-----------------+----------------+----------------+-----------------+
| > 09/07/2030    | > 0.036        | > 8            | > 81.517916     |
+-----------------+----------------+----------------+-----------------+
| > 10/07/2030    | > 0.036        | > 8            | > 81.517916     |
+-----------------+----------------+----------------+-----------------+
| > 11/07/2030    | > 0.036        | > 5.999648     | > 81.517916     |
+-----------------+----------------+----------------+-----------------+

***meanTimeCmar.csv***: average over all timesteps of the marginal
costs. 1 column per node, 1 row per scenario.

Table 21: meanTimeCmar.csv

  ------------------------------------------------------------------------
                                 RoGonDor      DolAmroth     Harad
  ------------------------------ ------------- ------------- -------------
  Base                           256.72732     3439.75537    1521.54793

  PVminus10                      257.017259    3583.34174    1793.57264

  Demandplus10                   442.220462    4878.66198    3086.87072

  PVminus10AndDemandplus10       451.32022     4977.57685    3259.88472
  ------------------------------------------------------------------------

***sortedCmar.csv***: average of the marginal costs histogram. 1 column
par node, 1 row per sorted time step index.

Table 22: SortedCmar.csv

+----------------+-----------------+-----------------+----------------+
|                | > **RoGonDor**  | > **DolAmroth** | > **Harad**    |
+================+=================+=================+================+
| > 0            | > 10000         | > 10000         | > 10000        |
+----------------+-----------------+-----------------+----------------+
| > 1            | > 10000         | > 10000         | > 10000        |
+----------------+-----------------+-----------------+----------------+
| > 2            | > 10000         | > 10000         | > 10000        |
+----------------+-----------------+-----------------+----------------+
| > 3            | > 10000         | > 10000         | > 10000        |
+----------------+-----------------+-----------------+----------------+
| > 4            | > 9512.5        | > 10000         | > 10000        |
+----------------+-----------------+-----------------+----------------+
| > 5            | > 9154.88089    | > 10000         | > 10000        |
+----------------+-----------------+-----------------+----------------+
| > 6            | > 9154.88089    | > 10000         | > 10000        |
+----------------+-----------------+-----------------+----------------+
| > 7            | > 8749.78       | > 10000         | > 10000        |
+----------------+-----------------+-----------------+----------------+
| > 8            | > 8506.03       | > 10000         | > 10000        |
+----------------+-----------------+-----------------+----------------+

***MarginalCostActivePowerDemand-NODE.csv***: marginal costs of the node
(in this case, the nodes on which the *ActivePowerDemand* constraints
apply). 1 column par scenario, 1 row per time step.

***HistCmar-NODE.csv*** : histogram of the marginal costs of the zone. 1
column par scenario, 1 row per sorted time step index.

##### Flows

***MeanImportExport-NODE.csv***: average import and exports to/from the
node. 1 column for Import, 1 column for export, 1 row per time step.

Table 23: meanImportExport-NODE.csv

  -----------------------------------------------------------------------
                          **Export**              **Import**
  ----------------------- ----------------------- -----------------------
  02/07/2030              0                       22488

  03/07/2030              0                       22488

  04/07/2030              0                       22488

  05/07/2030              0                       22488

  06/07/2030              0                       22488

  07/07/2030              0                       22488
  -----------------------------------------------------------------------

***ImportExport-NODE-\$i.csv***: import and exports to/from the node for
scenario \$i. 1 column for import, 1 column for export, 1 row per time
step.

***MeanImportExport.csv***: average flows. 1 column for import, 1 column
for line, 1 row per time step.

Table 24: MeanImportExport.csv

+-----------+----------------+--------------------+-------------------+
|           | > **DolA       | > **RoG            | > **              |
|           | mroth\>Harad** | onDor\>DolAmroth** | RoGonDor\>Harad** |
+===========+================+====================+===================+
| > 0       | > 1704         | > 52800            | > 20784           |
| 2/07/2030 |                |                    |                   |
+-----------+----------------+--------------------+-------------------+
| > 0       | > 1704         | > 52800            | > 20784           |
| 3/07/2030 |                |                    |                   |
+-----------+----------------+--------------------+-------------------+
| > 0       | > 1704         | > 52800            | > 20784           |
| 4/07/2030 |                |                    |                   |
+-----------+----------------+--------------------+-------------------+
| > 0       | > 1704         | > 52800            | > 20784           |
| 5/07/2030 |                |                    |                   |
+-----------+----------------+--------------------+-------------------+
| > 0       | > 1704         | > 52800            | > 20784           |
| 6/07/2030 |                |                    |                   |
+-----------+----------------+--------------------+-------------------+
| > 0       | > 1704         | > 52800            | > 20784           |
| 7/07/2030 |                |                    |                   |
+-----------+----------------+--------------------+-------------------+

