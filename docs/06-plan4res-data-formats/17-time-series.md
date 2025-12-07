# Time series

- **A set of CSV files containing scenarized time serie**s: those files follow a common format for time series: the first row is the header, the first column contains the UCT timestamp (in any format readable by [Python pandas](https://pandas.pydata.org/)) and the following columns are different scenarios of the current timeseries. One CSV file contains only timeseries for One variable. Scenarios are identified by the corresponding column name in the header line (for example, past years, eg 1970, 1971, 1972…);

Table 2: Example of stochastic timeserie

| 01101/01/2050 00:00111.60E-05111.60E-05111.76E-051101/01/2050 01:00111.60E-05111.60E-05111.76E-051101/01/2050 02:00111.60E-05111.60E-05111.76E-051101/01/2050 03:00111.60E-05111.60E-05111.76E-051101/01/2050 04:00111.60E-05111.60E-05111.76E-051101/01/2050 05:00111.60E-05111.60E-05111.76E-051101/01/2050 06:00113.31E-05113.31E-05113.64E-051101/01/2050 07:00114.91E-05114.91E-05115.40E-051101/01/2050 08:00116.51E-05116.51E-05117.16E-051101/01/2050 09:00118.11E-05118.11E-05118.92E-05 |

|---|

|  |  |  |

|  |

- **One (optional) unique CSV file containing all deterministic timeseries**: deterministic timeseries have to be present in a single csv file, whose name has to be given in the settingsCreateInputPlan4res_*xxx*.yml or in the settings_format_XXX.yml configuration file. This file follows the common format for time series: the first row is the header, the first column contains the UCT timestamp (in any format readable by [Python pandas](https://pandas.pydata.org/)) and the following columns correspond to each deterministic timeseries, the name of each deterministic timeseries being in the header.

Table 3: Deterministic time series

| 01101/01/2050 00:00112539999.7911235940.523111846508.331101/01/2050 01:00112330728.611202206.466111743163.671101/01/2050 02:00112400311.8111203914.562111762293.741101/01/2050 03:00112373790.7111200641.82111772480.461101/01/2050 04:00112242430.1811178585.198111578006.061101/01/2050 05:00112139597.0611167443.384111418207.691101/01/2050 06:00112524088.6711198991.4111717258.861101/01/2050 07:00112466338.4311200655.869111819359.651101/01/2050 08:00112339799.7311202049.705111839468.731101/01/2050 09:00112360725.9211201430.798111834015.731101/01/2050 10:00112311079.5611195961.933111815442.03 |

|---|

|  |  |  |

|  |