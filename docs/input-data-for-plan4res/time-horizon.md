### Time horizon

The time horizon needs to be specified. It usually is one year, but for
computing the strategies for management of seasonal storages it is
recommended to run the SSV module on a longer horizon, namely 18 months.
There is no restriction to using longer horizons, but it may lead to
very long computation times.

The user will then provide the following data (which may be different
for the different modules, providing that consistency is ensured):

-   Date/time of the first hour and last hour of the dataset

-   Date/time of the first hour and last hour with timeseries available

Note that it is possible to provide the input timeseries on a single
year. The CREATE and FORMAT modules will extend / duplicate the
timeseries to adapt to the requested period if the time series are not
available on the full period. As an example, we may have timeseries
available for the year 2018 only, and wish to run a study from Jan 1
2022 to June 30 2023. In that case the 2018 time series will be used 'as
if' they were representing 2023, and the first months will be duplicated
at the end of the year.

