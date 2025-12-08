## Plan4res csv Input Data

This section describes the format of plan4res input data. A dataset is
composed of 7 csv files representing the "fixed" data and of a number
timeseries (described in section 6.2).

All the CSV input files are following.

1.  One row containing column labels

2.  Serie of Rows containing the data (consistent with column labels)

3.  Each row contains a name, a zone and various values of variables.
    Zone can be any level of geographical partition (see below).

**Columns that are not used may be skipped.**

**Important notice:** within plan4res, the convention for the units is
that all data and results are in MW, MWh, €, €/MW, €/MWh depending on
the variable (see **Erreur ! Source du renvoi introuvable.** **Erreur !
Source du renvoi introuvable.**)

The dataset is composed of:

-   *ZP_ZonePartition.csv*: contains the description of the different
    regions;

-   *ZV_ZoneValues.csv*: contains the data linked to the regions (in
    particular the demand);

-   *IN_Interconnections.csv*: contains the description of the network;

-   *TU_ThermalUnits.csv*: contains the description of the thermal power
    plants (including nuclear) and of any asset which can be modeled in
    plan4res as a thermal plant (even if not using any fossil fuel)

-   *SS_SeasonalStorage.csv*: contains the description of hydropower
    with seasonal storages and other long-term seasonal storages;

-   *STS_ShortTermStorage.csv*: contains the description of all the
    short-term storages, including eg. pumped hydro, batteries but it
    can also be used for demand-response mechanisms such as
    load-shifting;

-   *RES_RenewableUnits.csv*: contains the description of PV, wind power
    and run-of-river technologies.

