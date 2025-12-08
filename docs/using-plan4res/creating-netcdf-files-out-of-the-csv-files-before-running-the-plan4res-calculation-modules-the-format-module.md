## Creating NetCDF files out of the csv files before running the plan4res calculation modules: the FORMAT module

The FORMAT module can be used as follows:

*p4r FORMAT YourDataset -M option1 -m option2*

option1 allows to choose which kind of NetCDF files will be created: for
running SSV (option1=optim), for running SIM (option1=simul), for
running CEM (option1=invest), or in the case where CEM has already be
ran and we want to create NetCDF files for SSV, based on the new
installed capacities as computed by CEM, option1=postinvest. (this is in
particular used in CEM -L, see below)

option1 is used only when option1=optim. It allows to specify which
csv_XXX to use for creating the NetCDF files for SSV.

FORMAT uses the python script format.py (in
P4R_DIR/p4r-env/scripts/python/plan4res-scripts).

format.py reads the csv plan4res input files (see section 6.3 for a
description of the format), and creates a serie of NetCdF files (in the
SMS++ format, see section 6.4) :

-   SDDPBlock.nc4: this file, used for optimisation, investment and
    simulation, describes the full problem, apart from investment ;

-   InvestmentBlock.nc4: this file, used for investment only, describes
    the investment problem.

-   N files Block_i.nc4: each one describes the assets for the SSV
    timestep i

When used with option -M postinvest, format.py also updates the data in
csv_simul and in csv_invest, and creates backup files for the original
data.

format.py requires 4 configuration files:

-   settings_format_XXX.yaml (see section 5.3.1.1)

-   settingsCreateInputPlan4res.yml (see section 5.2.2.1) which is also
    the main configuration file of CREATE.

-   VariablesDict.yml : contains the list of variables to retrieve and
    the correspondence between the plan4res and IAMC variable names (see
    section 5.2.2.3)

-   TimeSeriesDict: contains the list of timeseries to use for the
    different stochastic variables (described in the main configusation
    file) and regions (see section 5.2.2.2)

#### Filling the settings_format_XXX.yml file

The configuration files settings_format_optim.yml (for creation of
NetCDF files for SSV), settings_format_simul.yml (for creation of NetCDF
files for SIM), settings_format_invest.yml (for creation of NetCDF files
for CEM), or settings_format_postinvest.yml (for creation of NetCDF
files for SSV in the case of running SSV after CEM) define how the
NetCDF files will be created out of the plan4res CSV static data and
timeseries.

You may edit this file with any text editor. Change the following
parameters:

-   (do not change) **outputDir**: sub-directory of
    p4r-env/data/local/MY_STUDY/ where nc4 files are created (in
    practice nc4_optim, nc4_simul or nc4_invest)

-   (do not change) **inputDir**: sub-directory of
    p4r-env/data/local/MY_STUDY/ where csv files are (in practice
    csv_simul or csv_invest)

-   (do not change) (only in settings_format_postinvest.yml)
    **resultsDir**: sub-directory of p4r-env/data/local/MY_STUDY/ where
    the results of the capacity expansion (CEM) are located (in practice
    results_invest)

-   (do not change) (only in settings_format_postinvest.yml)
    **investDir**: sub-directory of p4r-env/data/local/MY_STUDY/ where
    the input csv files for the capacity expansion are (in practice
    csv_invest)

-   (do not change) **FormatMode**: defines which kinds of blocks are
    created: SingleUC : generates ONE UCBlock for the first period
    (first SSVTimestep) of the dataset, UC : generates a serie of
    UCBlocks for each period (each SSVTimestep) of the dataset, SDDP :
    generates only the SDDPBlock, SDDPandUC : generates the SDDPBlock
    and all the UCBlocks, INVEST : generates the InvestmentBlock,
    INVESTandSDDP : generates the InvestmentBlock and the SDDPBlock,
    INVESTandSDDPandUC : generates the InvestmentBlock and the SDDPBlock
    and all the UCBlocks; in practice modes SDDPandUC is used when
    running without investment and mode INVESTandSDDPandUC when running
    with investments.

-   (do not change) **FormatVU** defines the kind of bellman values used
    as inputs: None means that the bellman values are not included in
    the NetCDF files (they are passed as a separate file), PerReservoir
    means that 1 belmanvalue file per reservoir is used, and Polyhedral
    means that a single belmannvalues file for all reservoirs (with
    coefficients per reservoir) is used.

-   (do not change) **IncludeVU** defines at which ssv timestep bellman
    values are included: None means that no bellman values are used,
    Last means that they are used only at the last timestep and All
    means they are used at all timesteps.

-   **Invest** defines the additional constraints for investment
    optimization: Simple = no additional constraints are created, NRJ=
    regions are autonomous in energy (ie the amount of energy is
    sufficient for each node), TargetRES= each region has a target of
    renewable energies

-   **Calendar**: (see **Erreur ! Source du renvoi introuvable.**) this
    section is dedicated to the time data.

    -   **dayfirst**: True if the format is giving the day first
        (01/07/2050 means first of july)

    -   **BeginTimeSeries** : start of the available timeseries (in case
        the timeseries are available eg only for year 2050 and the
        dataset is created for 2030, the formatting tool will use anyway
        the timeseries and translate the dates)

    -   **EndTimeSeries** : end of the timeseries

    -   **BeginDataset** : first hour of the dataset in the NetCDF files

    -   **EndDataset**: end of the dataset in the NetCDF files

    -   **SSVTimeStep**: duration of the SSV timestep (eg 1 week); This
        duration is expressed as a number of XXX, where this number is
        given under **Duration** and XXX is the chosen "unit" (can be
        hours, days or weeks)

    -   **TimeStep**: duration of the timestep (eg 1 hour) (TimeStep is
        always lower or equal than SSVTimeStep). This duration is
        expressed as a number of XXX, where this number is given under
        **Duration** and XXX is the chosen "unit" (can be hours, days or
        weeks)

-   (do not change) **IncludeScenarisedData**: True or False wether
    scenarised data should be included in the Blocks (not necessary for
    running plan4res, but can be useful for running simulations on a
    single UCBlock). The data in the blocks will correspond to those of
    the first scenario.

-   **ParametersFormat:** this section gives a number of parameters

    -   **DownReservoirVolumeMultFactor**: multiplicative factor for
        computing the size of virtual downstream reservoir from the
        maximum volume of the upstream reservoir

    -   **DownDeltaRampUpMultFactor**: multiplicative factor for
        computing the maximum ramp up of the virtual downstream
        reservoir from the ramp up of upstream reservoir

    -   **DownDeltaRampDownMultFactor**: multiplicative factor for
        computing the maximum ramp down of the virtual downstream
        reservoir from the ramp down of the upstream reservoir

    -   **NumberHoursInYear**: number of hours in a year (8760). This is
        used for converting power to energy.

    -   **InertiaMultFactor**: multiplicative factor for computing the
        inertia contributions of the assets

    -   **Scenarios**: list of the scenarios to include in the instance
        (indexes of scenarios, among those available in the timeseries).
        It can include all scenarios that are available in all
        stochastic timeseries. It can also be only a subset.

    -   **ScenarisedData**: this section contains the list of scenarised
        data, among
        \'ActivePowerDemand\',\'Hydro:Inflows\',\'Renewable:MaxPowerProfile\'
        and \'Thermal:MaxPowerProfile\'; For each it must be specified
        wether the profile available in timeseries should be multiplied
        by an energy or a power in order to create the data. For the
        Renewable:MaxPowerProfile subsection, this information must be
        given for **res** (i.e. variable renewable energy, usually Wind
        and PV power) and for **runofriver.**

    -   **ThermalMaxPowerTimeSpan**: frequency of the data for
        scenarised thermal max power profiles. This is expressed as a
        duration, defined as a number of XXX, where this number is given
        under **Duration** and XXX is the chosen "unit" (can be hours,
        days or weeks). For example, 168 hours means that the same value
        of the scenarios for \'Thermal:MaxPowerProfile will be used each
        week. These scenarios thus do not need to have a higher
        granularity.

    -   **CoeffSpillage**: it is allowed to spill CoeffSpillage\*Maximum
        Flow

    -   **LowerBound**: optional: lower bound for the SDDP algorithm in
        SSV. This is optional.

    -   (do not change) **RecomputeCSV**: True if it is required that
        format.py will compute new CSV files in csv_simul and csv_invest
        to account for new installed capacities as computed by CEM. This
        is used only in settings_format_postinvest.yml. If it is not
        present it is assumed to be False.

    -   **RoundDecimals**: number of decimals to keep for rounding
        values.

