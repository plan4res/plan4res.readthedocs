### Dataset directory

Figure 3 shows the structure of plan4res.

Figure 3: structure of data

Each dataset corresponds to a directory in data (here toyDataset,
Otherdataset1 and OtherDataset2). Datasets always have the same
structure:

-   Timeseries: contains the timeseries which are used as inputs, as
    well as the timeseries created by the data treatments of plan4res --
    the CREATE module- (aggregated timeseries over regions, or
    timeseries with a different time granularity)

-   IAMC: contains the scenario which can be used to create the plan4res
    input data (this can be a result of an energy modelling tool such as
    e.g. GENeSYS-MOD. The dataset used must be a csv file named
    DATASE.csv. It must comply to the IAMC format[^12].

-   csv_simul and csv_invest: those 2 sub repositories contain the
    native input files of plan4res. These can be created manually by the
    user or from a scenario in IAMC/ by using the CREATE module of
    plan4res. csv_simul contains files which cannot be used for
    performing an investment study, while csv_invest contains files
    which can be used for performing an investment study. The difference
    between those 2 sets of files lies in the fact that csv_invest may
    include some generation assets which are described only because it
    is allowed to invest in these units, while their capacity is 0. As
    the investment module (CEM) can only increase the existing
    capacities, it is necessary to start from a dataset with all
    possible technologies. The 'new' technologies are then present but
    with a very low capacity (whose level is defined in the plan4res
    settings files).

-   nc4_optim, nc4_simul and nc4_invest: these 3 sub repositories
    contain the plan4res NetCDF inputs, which are created from the data
    in csv_XXX/ and in Timeseries/ by the FORMAT module of plan4res.
    These datasets are not easily readable so the user may not look at
    them.

-   results_optim: This repo will contain the results of the SSV module

-   results_simul: This repo will contain the results of the SIM module

-   results_invest: This repo will contain the results of the CEM module

-   settings: This repo contains all the configuration files used by all
    different modules of plan4res.

The data generation modules CREATE and FORMAT as well as the solving
modules SSV, SIM and CEM also create the directories when they are not
yet present. It is then possible to run CREATE when only IAMC and
Timeseries are present, or FORMAT when only Timeseries and csv_simul are
present.

