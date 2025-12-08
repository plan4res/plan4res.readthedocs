### Data for the power system

#### Interconnections

**The list of interconnections between nodes**, with for each
interconnection:

-   **The node where the interconnection starts**

-   **The node where the interconnection ends**

-   **The maximum power flow in MW** (Network\|Electricity\|Maximum
    Flow)

-   **The minimum power flow in MW**

-   (optional) the impedance of the line

-   (optional) the cost of using the line (in €/MWh)

-   (optional) **the investment cost (in €/MW)**
    (Network\|Electricity\|Expansion Cost)

#### Generation

##### Thermal generation

Thermal generation includes all kinds of generation units which can be
modelled as a Thermal Unit in plan4res. In particular it includes all
traditional generation units running on fossil fuels (coal, gaz, oil),
but also biomass units, nuclear units as well as geothermal units.

The generation mix can be described either unit per unit, or technology
per technology. The following data are necessary for each unit /
technology

-   **Capacity** **(MW) of the technology (if provided per technology,
    this needs to be given for each node). Can be provided as a
    deterministic timeseries if depending on time.**
    (Capacity\|Electricity\|)

```{=html}
<!-- -->
```
-   (optional) Maximum Power of the unit, or of an individual unit if
    provided per technology (MW) ; Can be provided as a deterministic
    timeseries if depending on time.

```{=html}
<!-- -->
```
-   **Variable Cost (including fuel cost)** **(€/MWh); Can be provided
    as a deterministic timeseries if depending on time.** (Variable Cost
    (incl. Fuel Cost)\|Electricity\|)

-   (optional) **Fixed Cost** **(€) ; Can be provided as a deterministic
    timeseries if depending on time.** (Fixed Cost\|Electricity\|)

```{=html}
<!-- -->
```
-   (optional) Quadratic cost (€/Mwh\^2); Can be provided as a
    deterministic timeseries if depending on time.

```{=html}
<!-- -->
```
-   **Investment Cost** **(€/MW); Can be provided as a deterministic
    timeseries if depending on time.** (Capital Cost\|Electricity\|)

```{=html}
<!-- -->
```
-   (optional) Minimum Power of the unit (MW) (or of an individual unit
    if provided per technology, or for the whole aggregated technology);
    Can be provided as a deterministic timeseries if depending on time.

-   (optional) Auxiliary power, ie consumption when started but
    producing 0 (MW)

-   (optional) Start up cost (€) for starting the unit after a
    shut-down.

-   (optional) Minimum time down (hours)

-   (optional) Minimum time up (hours)

-   (optional) Ramping up and down, ie maximum gradients for power
    increase/decrease (MW per hour)

-   (optional) Inertia that the unit can provide in MWs/MWA

-   (optional) Share of the maximum power that can be devoted to the FCR

-   (optional) Share of the maximum power that can be devoted to the
    AFRR

-   (optional) Forced outage rate

-   (optional) Planned outage rate (or schedules for planned outages)

-   (optional) Mean outage duration (hours)

```{=html}
<!-- -->
```
-   (optional) **CO2 emissions (tons per MWh)** (Emission
    Rate\|CO2\|Electricity\|)

```{=html}
<!-- -->
```
-   (optional) other pollutant emissions

It is possible to account for scenarios of available power for the
thermal units. These must then be provided as stochastic timeseries per
unit (or per technology) and node.

##### Hydro power

3 categories of Hydro Power can be represented in plan4res:

-   Seasonal storage, corresponding to the hydro power with large
    reservoirs, which are operated over the year

-   Pumped Hydro, corresponding to hydro power with pumping capacity,
    and medium size storages, operated on short term periods

-   Run of river, corresponding to hydro power without reservoirs.

###### Seasonal storage

Seasonal storage is usually described as an aggregated unit per node. It
can be disaggregated but this may increase a lot the computation time.
The following data are necessary for each unit:

-   **Capacity** **(MW) of the technology.** Can be provided as a
    deterministic timeseries if depending on time.
    (Capacity\|Electricity\|Reservoir)

-   (optional) if disaggregated, Maximum Power in MW or Maximum Flow (in
    MW) of each unit

-   **Maximum volume of the storage in MWh.** Can be provided as a
    deterministic timeseries if depending on time. (Maximum
    Storage\|Electricity\|Reservoir)

-   (optional) As the seasonal storages are managed in MWh, it is
    assumed that the Minimum Volume is 0, but this data can also be
    provided as a number or a timeseries.

-   (optional) Inertia that the unit can provide in MWs/MWA

-   (optional) Share of the maximum power that can be devoted to the FCR

-   (optional) Share of the maximum power that can be devoted to the
    AFRR

```{=html}
<!-- -->
```
-   **Inflows to the reservoir in MWh. This must be provided as
    timeseries, if possible stochastic timeseries (ie a number of
    scenarios). The time granularity may be hourly or bigger. The
    timeseries can be profiles which will be used to distribute the
    yearly inflows in MWh over the period. These profiles must have the
    following characteristics: the expectancy on all scenarios of the
    sum of the values over one year is equal to 1. If we know the
    expected volume of inflows in MWh on the given year, we can then use
    those profiles to compute representative inflows scenarios by
    multipliying the profiles by the total inflows.** **The energy
    produced by reservoir hydro** Secondary
    Energy\|Electricity\|Reservoir **in the GENeSYS-MOD scenario is a
    good approximation of the total Inflows.**

-   (optional) Efficiency: this coefficient will be applied to the flow
    from the reservoir to compute the power generation. If not present
    it will be assumed to be 1.

-   If the seasonal storage has some pumping capacity, there also need
    to be provided the Minimum Flow or minimum power (which is
    negative), as well as the pumping efficiency (which should be lower
    than 1)

-   (optional) Ramping up and down, ie maximum gradients for power
    increase/decrease (MW per hour)

-   (optional) Inertia that the unit can provide in MWs/MWA

-   (optional) Share of the maximum power that can be devoted to the FCR

-   (optional) Share of the maximum power that can be devoted to the
    AFRR

-   **Volume in the reservoir at the beginning of the study in MWh**

###### Pumped Hydro

Pumped hydro is usually described as an aggregated unit per node. It can
also be disaggregated:

-   **Capacity in MW.** Can be provided as a deterministic timeseries if
    depending on time. (Capacity\|Electricity\|Pumped Storage)

-   (optional) if disaggregated, Maximum Power in MW or Maximum Flow (in
    MW) of each unit

-   **(optional) Minimum power or Minimum Flow in MW (=maximum
    pumping).** Can be provided as a deterministic timeseries if
    depending on time. If not provided, assumed to be equal to Capacity
    \* pumping efficiency

-   **Maximum volume of the storage in MWh.** Can be provided as a
    deterministic timeseries if depending on time. (Maximum
    Storage\|Electricity\|Pumped Storage)

-   (optional) As the pumped storages are managed in MWh, it is assumed
    that the Minimum Volume is 0, but this data can also be provided as
    a number or a timeseries.

-   **Efficiency when turbining.** Can be provided as a deterministic
    timeseries if depending on time. (Pumping
    Efficiency\|Electricity\|Pumped Storage)

-   **Pumping efficiency.** Can be provided as a deterministic
    timeseries if depending on time. (Charging
    Efficiency\|Electricity\|Pumped Storage)

-   **Investment Cost** **(€/MW); Can be provided as a deterministic
    timeseries if depending on time.** (Capital
    Cost\|Electricity\|Pumped Storage)

-   (optional) Inertia that the unit can provide in MWs/MWA

-   (optional) Share of the maximum power that can be devoted to the FCR

-   (optional) Share of the maximum power that can be devoted to the
    AFRR

```{=html}
<!-- -->
```
-   (optional) Inflows to the reservoir in MWh. This can be provided as
    number in MWh (which will be linearly distributed to the timesteps)
    or as a deterministic timeseries.

-   (optional) Ramping up and down, ie maximum gradients for power
    increase/decrease (MW per hour)

-   (optional) Cost in €/MWh

-   (optional) Volume level target at the end of the SSV time step (in
    that case, it will be ensured that at the end of each SSV timestep,
    the reservoir reaches this target.

-   **Volume in the reservoir at the beginning of the study in MWh**

###### Run of river

Run of river is usually described as an aggregated unit per node. It can
also be disaggregated, but the results will be similar (with longer
computation times)

-   **Capacity in MW.** (Capacity\|Electricity\|Run of River)

-   **Investment Cost** **(€/MW); Can be provided as a deterministic
    timeseries if depending on time.** (Capital Cost\|Electricity\| Run
    of River)

-   Power profiles. This must be provided as timeseries, if possible
    stochastic. These profiles will be multiplied by the Capacity to
    create Maximum Power timeseries. If stochastic profiles are used
    they must comply to the rule all values must be between 0 and 1, and
    the average of all values is the load factor of the technology.

-   (optional) Minimum power in MW (=maximum pumping). Can be provided
    as a deterministic timeseries if depending on time. If not provided,
    assumed to be equal to 0

-   (optional) Inertia that the unit can provide in MWs/MWA

-   (optional) Share of the maximum power that can be devoted to the FCR
    and the AFRR

##### Variable renewable

Variable renewable includes Solar Power and Wind Power. They must be
described per technology when the technologies have different
characteristics.

Each technology is usually described as an aggregated unit per node. It
can also be disaggregated, but the results will be similar (with longer
computation times)

-   **Capacity in MW.** (Capacity\|Electricity\| )

-   **Investment Cost** **(€/MW); Can be provided as a deterministic
    timeseries if depending on time.** (Capital Cost\|Electricity\| )

-   Power profiles. This must be provided as timeseries, if possible
    stochastic. These profiles will be multiplied by the Capacity to
    create Maximum Power timeseries. If stochastic profiles are used
    they must comply to the rule all values must be between 0 and 1, and
    the average of all values is the load factor of the technology.

-   (optional) Minimum power in MW (=maximum pumping). Can be provided
    as a deterministic timeseries if depending on time. If not provided,
    assumed to be equal to 0

-   (optional) Share of the maximum power that can be devoted to the FCR
    and the AFRR

##### Short term storage (excluding hydro)

This category is mostly used for describing the different battery
technologies, but may be used for any kind of electricity storage. This
technology should be disaggregated as much as possible in order not to
over estimate the flexibility that it provides.

-   **Capacity in MW.** Can be provided as a deterministic timeseries if
    depending on time. (Capacity\|Electricity\|)

-   (optional) if disaggregated, Maximum Power in MW or Maximum Flow (in
    MW) of each unit

-   **Investment Cost** **(€/MW); Can be provided as a deterministic
    timeseries if depending on time.** (Capital Cost\|Electricity\| )

-   **(optional) Minimum power or Minimum Flow in MW (=maximum
    pumping).** Can be provided as a deterministic timeseries if
    depending on time. If not provided, assumed to be equal to Capacity
    \* pumping efficiency

-   **Maximum volume of the storage in MWh.** Can be provided as a
    deterministic timeseries if depending on time. (Maximum
    Storage\|Electricity\|)

-   (optional) As the pumped storages are managed in MWh, it is assumed
    that the Minimum Volume is 0, but this data can also be provided as
    a number or a timeseries.

-   **Efficiency when charging/discharging.** Can be provided as a
    deterministic timeseries if depending on time. (Charging
    Efficiency\|Electricity\| ) (Discharging Efficiency\|Electricity\| )

-   (optional) Inertia that the unit can provide in MWs/MWA

-   (optional) Share of the maximum power that can be devoted to the FCR

-   (optional) Share of the maximum power that can be devoted to the
    AFRR

```{=html}
<!-- -->
```
-   (optional) Inflows to the storage in MWh or Demands from that
    storage (negative values). This can be used to represent e.g. the
    consumption of electric vehicles if modelling their batteries as a
    storage. This can be provided as number in MWh (which will be
    linearly distributed to the timesteps) or as a deterministic
    timeseries.

-   (optional) Ramping up and down, ie maximum gradients for power
    increase/decrease (MW per hour)

-   (optional) Cost in €/MWh

-   (optional) Storage level target at the end of the SSV time step (in
    that case, it will be ensured that at the end of each SSV timestep,
    the reservoir reaches this target.

-   **(optional) Volume in the reservoir at the beginning of the study
    in MWh**

#### Other flexibilities

Flexibilities such as load shifting can be represented as short term
storages. The periods on which some demand can be shifted can be managed
via the Minimum Storage and Maximum Storage data.

