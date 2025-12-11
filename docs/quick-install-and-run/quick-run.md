## Quick Run

-   **Create dataset in P4R_DIR_LOCAL/data** (e.g. YourDataset), with a
    subdirectory IAMC, a subdirectory settings and a subdirectory
    TimeSeries␣␣


-   **Move your IAMC file** (as computed by GENeSYS-MOD for instance) in
    P4R_DIR_LOCAL/data/IAMC/ and rename it  P4R_DIR_LOCAL/data/IAMC/YourDataset.xlsx␣␣


-   **Copy the settings files** from P4R_DIR_LOCAL/data/toyDatasetsettings/
    to P4R_DIR_LOCAL/data/settings/␣␣


-   **Create or get and Upload your timeseries** to P4R_DIR_LOCAL/data/TimeSeries␣␣


-   **Edit configuration files** in P4R_DIR_LOCAL/data/settings:

    -   Edit settingsCreatePlan4res.yml (in particular the IAMC
        scenario and year, the list of regions, the regions partitions,
        the list of technologies, the list of scenarios, the definition
        of coupling constraints, the initial filling rates, the
        (optional) parameters for capacity expansion, and if necessary
        the list of variables to use from your IAMC file)

    -   Edit DictTimeSeries.yml (so that is has the good names for your
        timeseries)

    -   If necessary (if you have changed some variable names in
        settingsCreatePlan4res.yml), edit the
        VariablesDictionnary.yml␣␣


-   **Run CREATE:**
 ```bash
     p4r CREATE YourDataset -M simul    # for a case without capacity expansion
     p4r CREATE YourDataset -M invest   # for a case with capacity expansion
   ```
␣␣

-   **Edit settings_format_optim.yml, settings_format_simul.yml and
    settings_format_invest.yml** configuration files in P4R_DIR_LOCAL/data/settings/ (in
    particular the sections Calendar, and the Scenarios and
    ScenarisedData in section ParametersFormat)␣␣


-   **Run SSV:** 
 ```bash
     p4r SSV YourDataset
   ```
␣␣

-   **Run SIM:**
 ```bash
     p4r SIM YourDataset
   ```
␣␣

-   **Run CEM:** 
 ```bash
     p4r CEM YourDataset
   ```
␣␣

-   **Edit settingsPostTreatPlan4res.yml**  in P4R_DIR_LOCAL/data/settings/. In particular, the
    start and end dates of you study, the list of technologies (if you
    added new technologies), and the size of graphs (to allow to cope
    with all regions / all interconnections / all technos)
␣␣

-   **Run POSTTREAT:** 
 ```bash
     p4r POSTTREAT YourDataset -M simul    # for a case without capacity expansion
     p4r POSTTREAT YourDataset -M invest   # for a case with capacity expansion
   ```
