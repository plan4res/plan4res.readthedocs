### File SS_SeasonalStorage.csv

This file gives the characteristics of all seasonal storages. Only
aggregated seasonal storages (ie one with one reservoir) can be
described in this file (although SMS++ is capable of handling complex
hydrovalleys).

Table 9: SS_SeasonalStorage.csv

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 8%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 5%" />
<col style="width: 8%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 7%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Name</strong></th>
<th><strong>Zone</strong></th>
<th><p><strong>Hydro</strong></p>
<p><strong>System</strong></p></th>
<th><p><strong>Number</strong></p>
<p><strong>Units</strong></p></th>
<th><p><strong>Max</strong></p>
<p><strong>Power</strong></p></th>
<th><p><strong>Min</strong></p>
<p><strong>Power</strong></p></th>
<th><p><strong>Max</strong></p>
<p><strong>Volume</strong></p></th>
<th><p><strong>Min</strong></p>
<p><strong>Volume</strong></p></th>
<th><strong>Inflows</strong></th>
<th><p><strong>Inflows</strong></p>
<p><strong>Profile</strong></p></th>
<th><p><strong>Initial</strong></p>
<p><strong>Volume</strong></p></th>
<th><p><strong>Turbine</strong></p>
<p><strong>Efficiency</strong></p></th>
<th><p><strong>Pumping</strong></p>
<p><strong>Efficiency</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Hydro|Reservoir</td>
<td>RoGonDor</td>
<td>0</td>
<td>1</td>
<td>25814.05</td>
<td>0</td>
<td>51628100</td>
<td>0</td>
<td>7.5E+07</td>
<td><p>Inflows_Ro</p>
<p>GonDor.csv</p></td>
<td>34418733.3</td>
<td>1</td>
<td>0</td>
</tr>
<tr class="even">
<td>Hydro|Reservoir</td>
<td>DolAmroth</td>
<td>0</td>
<td>1</td>
<td>5524.2394</td>
<td>0</td>
<td>11048478.9</td>
<td>0</td>
<td>1.6E+07</td>
<td><p>Inflow_Dol</p>
<p>Amroth.csv</p></td>
<td>6629087.33</td>
<td>1</td>
<td>0</td>
</tr>
<tr class="odd">
<td>Hydro|Reservoir</td>
<td>Harad</td>
<td>0</td>
<td>1</td>
<td>6000</td>
<td>0</td>
<td>12000000</td>
<td>0</td>
<td>2.8E+07</td>
<td><p>Inflow_</p>
<p>Harad.csv</p></td>
<td>6000000</td>
<td>1</td>
<td>0</td>
</tr>
</tbody>
</table>

It contains the following columns (*Note that all numerical values may
be replaced by the name of a deterministic Timeserie*):

-   **Name**: name of the technology, or name of the plant. The list of
    > names must be present in the
    > settingsCreateInputPlan4res\_*xxx*.yml configuration file (technos
    > section, reservoir), as this list is used in particular for
    > post-treatments of results. Whenever the user wishes to add a new
    > technology or plant, it must be added to the list in the
    > settingsCreateInputPlan4res\_*xxx*.yml configuration file.

-   **Zone**: the values in this column must be included in the list of
    > **nodes**, which is given in the first column of
    > ZP_ZonePartition.csv, and corresponds to the lowest granularity of
    > regions.

-   **NumberUnits**: number of units of the same type at the same
    > location.

-   **MaxPower** : maximum power of a single unit in MW. When
    > NumberUnits=1, MaxPower is equal to Capacity. Can be a
    > deterministic timeserie.

-   **MinPower**[^25] (optional, 0 by default) [^26] : minimum power of
    > a single unit in MW. Can be a deterministic timeseries. *This
    > constraint is relaxed in SSV and CEM, as well as in SIM when the
    > user requires to use continuous relaxation (see parameter in SMS++
    > configuration files)*

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

-   **MaxVolume** : maximum volume of the reservoir (MWh). Can be a
    > deterministic timeseries.

-   **MinVolume**[^27] (optional, 0 by default) : minimum volume of the
    > reservoir (MWh). Can be a deterministic timeseries.

-   **TurbineEfficiency**: (optional, 1 by default). This value,
    > multiplied by the flow, gives the generated power.

-   **PumpingEfficiency**: (optional, 1 by default, but should be lower
    > than TurbineEfficiency in practice). This value, multiplied by the
    > flow, gives the generated power.

-   **Inflows**: (optional, 0 by default; mandatory if column
    > InflowsProfile is present). Inflows to the upstream reservoir
    > (energy per year in MWh).

-   **InflowsProfile**: (optional): time series profile for Inflows.
    > Multiplied by the Inflows in energy, gives the inflows time
    > series. These timeseries may be stochastic (in that case the value
    > has to be XXX.csv), or deterministic.

-   **InitialVolume**: (optional, 0 by default). Initial Volume of the
    > upstream reservoir (MWh)

-   **Inertia** (optional, 0 by default): maximum inertia that can be
    > provided by a unit in MWs/MWA. Can be a deterministic timeseries.

-   **PrimaryRho**: (%) this parameter, multiplied by MaxPower, gives
    > the maximum primary reserve that can be provided by a unit
    > (optional, 0 by default). Can be a deterministic timeserie.

-   **SecondaryRho**: (%) this parameter, multiplied by MaxPower, gives
    > the maximum secondary reserve that can be provided by a unit
    > (optional, 0 by default). Can be a deterministic timeserie.

-   **WaterValues**: optional; used to specify water values as input
    > data from a file, if they are/were not computed by the current run
    > (for example, coming from a previous SSV run). Contains the name
    > of the file/sheet where the water values are stored. When using
    > the simulation mode with one Bellman values (BV) file for all
    > units (ie a polyhedral function), this file is only given in the
    > first line; when using the simulation mode with 1 BV per unit (ie
    > one function per reservoir), this file is given at each line; in
    > optimization mode (= when running the SSV), this is not used as
    > computed by the model. This column is always optional as the BV
    > file (in case it is a polyhedral function) can be passed to SMS++
    > when calling the solver.

