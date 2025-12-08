### Demands

#### Power demand

The power demand must be given for each node. As much as possible it is
better to provide it as stochastic timeseries, and if possible to
disaggregate it per uses. The following data are necessary:

-   Demand per uses

    -   Demand for electric heating:

        -   **Demand in MWh over the whole year** (Final
            Energy\|Electricity\|Heating)

        -   **Time series , if possible stochastic. The time granularity
            should be hourly. The timeseries should be profiles which
            will be used to distribute the yearly demand in MWh over the
            period. These profiles must have the following
            characteristics: the expectancy on all scenarios of the sum
            of the values over one year is equal to 1. If we know the
            expected demand in MWh on the given year, we can then use
            those profiles to compute representative demand scenarios by
            multipliying the profiles by the total demand.**

    -   Demand for cooling

        -   **Demand in MWh over the whole year** (Final
            Energy\|Electricity\|Cooling)

        -   **Time series, if possible stochastic. (same characteristics
            as for electric heating)**

    -   Demand for electric transport

        -   **Demand in MWh over the whole year** (Final
            Energy\|Electricity\|Transportation)

        -   **Time series, usually deterministic but can be stochastic.
            (same characteristics as for electric heating). Timeseries
            over 1 day could be sufficient if there is no seasonality.**

    -   Demand for electric cooking

        -   **Demand in MWh over the whole year** (Final
            Energy\|Electricity\|Cooking)

        -   **Time series, usually deterministic but can be stochastic.
            (same characteristics as for electric heating). Timeseries
            over 1 day could be sufficient if there is no seasonality.**

    -   Demand for other uses of electricity

        -   **Demand in MWh over the whole year** (Final
            Energy\|Electricity\|Other (excl. ...)

        -   **Time series, usually deterministic but can be stochastic.
            (same characteristics as for electric heating). Timeseries
            over 1 day could be sufficient if there is no seasonality.**

-   Or if the demand per uses is not available, total demand:

    -   **Demand in MWh over the whole year** (Final
        Energy\|Electricity)

    -   **Time series, if possible stochastic. (same characteristics as
        for electric heating)**

#### (optional) Reserves

(optional) The requested level of reserves (FCR, AFFR or aggregated) per
region (which could be groups of nodes) or per node, either in share of
the power demand, or in MWh, as a timeseries.

