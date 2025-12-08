## Time series

-   **A set of CSV files containing scenarized time serie**s: those
    > files follow a common format for time series: the first row is the
    > header, the first column contains the UCT timestamp (in any format
    > readable by [Python pandas](https://pandas.pydata.org/)) and the
    > following columns are different scenarios of the current
    > timeseries. One CSV file contains only timeseries for One
    > variable. Scenarios are identified by the corresponding column
    > name in the header line (for example, past years, eg 1970, 1971,
    > 1972...);

Table 2: Example of stochastic timeserie

+-----------------------+--------------+------------+-----------------+
| > Timestamp \[UTC\]   | > Base       | >          | > Demandplus10  |
|                       |              |  PVminus10 |                 |
+=======================+==============+============+=================+
| > 01/01/2050 00:00    | > 1.60E-05   | > 1.60E-05 | > 1.76E-05      |
+-----------------------+--------------+------------+-----------------+
| > 01/01/2050 01:00    | > 1.60E-05   | > 1.60E-05 | > 1.76E-05      |
+-----------------------+--------------+------------+-----------------+
| > 01/01/2050 02:00    | > 1.60E-05   | > 1.60E-05 | > 1.76E-05      |
+-----------------------+--------------+------------+-----------------+
| > 01/01/2050 03:00    | > 1.60E-05   | > 1.60E-05 | > 1.76E-05      |
+-----------------------+--------------+------------+-----------------+
| > 01/01/2050 04:00    | > 1.60E-05   | > 1.60E-05 | > 1.76E-05      |
+-----------------------+--------------+------------+-----------------+
| > 01/01/2050 05:00    | > 1.60E-05   | > 1.60E-05 | > 1.76E-05      |
+-----------------------+--------------+------------+-----------------+
| > 01/01/2050 06:00    | > 3.31E-05   | > 3.31E-05 | > 3.64E-05      |
+-----------------------+--------------+------------+-----------------+
| > 01/01/2050 07:00    | > 4.91E-05   | > 4.91E-05 | > 5.40E-05      |
+-----------------------+--------------+------------+-----------------+
| > 01/01/2050 08:00    | > 6.51E-05   | > 6.51E-05 | > 7.16E-05      |
+-----------------------+--------------+------------+-----------------+
| > 01/01/2050 09:00    | > 8.11E-05   | > 8.11E-05 | > 8.92E-05      |
+-----------------------+--------------+------------+-----------------+

-   **One (optional) unique CSV file containing all deterministic
    > timeseries**: deterministic timeseries have to be present in a
    > single csv file, whose name has to be given in the
    > settingsCreateInputPlan4res\_*xxx*.yml or in the
    > settings_format_XXX.yml configuration file. This file follows the
    > common format for time series: the first row is the header, the
    > first column contains the UCT timestamp (in any format readable by
    > [Python pandas](https://pandas.pydata.org/)) and the following
    > columns correspond to each deterministic timeseries, the name of
    > each deterministic timeseries being in the header.

Table 3: Deterministic time series

  -------------------------------------------------------------------------
  **Timestamp \[UTC\]**     **TS_XX**       **TS_YY**       **TS_ZZ**
  ------------------------- --------------- --------------- ---------------
  01/01/2050 00:00          2539999.79      235940.523      1846508.33

  01/01/2050 01:00          2330728.6       202206.466      1743163.67

  01/01/2050 02:00          2400311.81      203914.562      1762293.74

  01/01/2050 03:00          2373790.71      200641.82       1772480.46

  01/01/2050 04:00          2242430.18      178585.198      1578006.06

  01/01/2050 05:00          2139597.06      167443.384      1418207.69

  01/01/2050 06:00          2524088.67      198991.4        1717258.86

  01/01/2050 07:00          2466338.43      200655.869      1819359.65

  01/01/2050 08:00          2339799.73      202049.705      1839468.73

  01/01/2050 09:00          2360725.92      201430.798      1834015.73

  01/01/2050 10:00          2311079.56      195961.933      1815442.03
  -------------------------------------------------------------------------

