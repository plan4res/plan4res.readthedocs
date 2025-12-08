## Creating a plan4res dataset

A plan4res dataset is composed of a number of 'static' CSV files (where
static means that these data do not include timeseries) describing the
power system ("static" data) and of a number of timeseries (in
particular the power demand, inflows, RES potentials hourly -- and
stochastic- timeseries).

-   **The static CSV plan4res input data files**: see the list of data
    required in the document plan4resInputData[^15] and a description of
    the format of the static csv files in the document
    plan4resDataFormats^16^.

There are 2 ways of creating the static CSV files:

-   You can manually create the required csv_files[^16] in
    P4R_DATA_LOCAL/data/YourDataset/csv_simul or
    P4R_DATA_LOCAL/data/YourDataset/csv_invest

-   You can create the csv_files from a dataset in IAMC format (see
    example in toyDataset/IAMC) using the plan4res command p4r CREATE
    YourDataset. This requires that a IAMC data excel file named
    YourDataset.xlsx is available in
    P4R_DATA_LOCAL/data/YourDataset/IAMC

```{=html}
<!-- -->
```
-   **The timeseries** may be historics or forecasts. Most of them can
    be found in the Copernicus Climate Change Service Data Store[^17].

See section 6.3 for the formats of the data files.

