
A dataset must first be created in P4R_DIR_LOCAL /data. The name of the
sub-directory in P4R_DIR_LOCAL /data must be the name of the dataset. An
example is given with P4R_DIR_LOCAL /data/toyDataset which is created
during the install process.

Once a dataset is created, you can start running the different plan4res
modules using the plan4res commands p4r or sp4r (if running on a cluster
with SLURM[^13]). The commands p4r and sp4r (see section 5.1) are
installed during the installation process.

In summary, to conduct a case study, the following steps may be
followed:

-   **Create a plan4res dataset**:

    -   This can be done from a IAMC file (created by GENeSYS-MOD or any
        other tool) using the command *p4r CREATE YourDataset -M simul*
        (or p4r CREATE YourDataset -M invest)

    -   Or it can be done by editing manually the CSV files.

    -   A plan4res dataset is composed of

        -   a set of CSV static files in
            P4R_DIR_LOCAL/data/YourDataset/csv_invest (for studies with
            capacity expansion) or in
            P4R_DIR_LOCAL/data/YourDataset/csv_simul (for studies
            without capacity expansion)

        -   AND a set of timeseries in
            > P4R_DIR_LOCAL/data/YourDataset/TimeSeries

-   **Run the formatting module to create NetCDF files** for the
    seasonal storage required by SMS++:

    -   *p4r FORMAT YourDataset -M optim -m simul*

    -   OR *p4r FORMAT YourDataset -M optim -m invest*

    -   Depending if you are creating these files from the data in
        csv_simul or in csv_invest

-   **Run the seasonal storage valuation**: *p4r SSV YourDataset*

-   **Run the formatting module to create NetCDF files** for the
    simulation (this requires that SSV has been ran first as the results
    of SSV are used): *p4r FORMAT YourDataset -M simul*

-   **Run the simulation**: *p4r SIM YourDataset*

-   **Run the formatting module to create NetCDF files** for the
    capacity expansion (this requires that SSV has been ran first as the
    results of SSV are used): *p4r FORMAT YourDataset -M invest*

-   **Run the capacity expansion**: *p4r CEM YourDataset*

-   **Post-treat the results**:

    -   *P4r POSTTREAT YourDataset -M simul* (for simulation results)

    -   *P4r POSTTREAT YourDataset -M simul* (for simulation results)

The workflow is shown in Figure 4: plan4res workflow.

