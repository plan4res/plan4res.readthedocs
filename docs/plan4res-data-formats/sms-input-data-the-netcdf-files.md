## SMS++ input data: the NetCDF files

The CSV static data files and timeseries are converted into the
following NetCDF files, following the specifications[^33] of those files
defined by SMS++.

3 different kinds of NetCDF files are created:

-   Block\_\$i.nc4: these files (one per SSV timestep) are describing
    the power system in the current timestep

-   SDDPBlock.nc4: this file is describing the SSV problem, including
    all stochastic scenarios

-   InvestmentBlock.nc4: this file is describing the CEM problem, with
    in particular identification of the assets which can be invested and
    related constraints

