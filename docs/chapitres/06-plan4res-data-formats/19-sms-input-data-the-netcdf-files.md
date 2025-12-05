# SMS++ input data: the NetCDF files

The CSV static data files and timeseries are converted into the following NetCDF files, following the specifications[https://gitlab.com/smspp/smspp-project/-/raw/develop/doc/SMS++%20File%20Format%20Manual/ffm.pdf?ref_type=heads](https://gitlab.com/smspp/smspp-project/-/raw/develop/doc/SMS++%20File%20Format%20Manual/ffm.pdf?ref_type=heads) of those files defined by SMS++.

3 different kinds of NetCDF files are created:

- Block_$i.nc4: these files (one per SSV timestep) are describing the power system in the current timestep

- SDDPBlock.nc4: this file is describing the SSV problem, including all stochastic scenarios

- InvestmentBlock.nc4: this file is describing the CEM problem, with in particular identification of the assets which can be invested and related constraints