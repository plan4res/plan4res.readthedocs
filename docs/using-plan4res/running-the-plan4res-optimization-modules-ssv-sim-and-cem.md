## Running the plan4res optimization modules SSV, SIM and CEM

These 3 modules are the main components of plan4res. They correspond to
executables of the SMS++ library. They are all launched using p4r MODULE
YourDataSet. A number of options can be added to this command (see
section 5.1.1), in particular -C (to force use of CREATE first) and -F
(to force use of FORMAT first) and -o Dir (to write the results in a
sub-directory Dir of results_XXX/) . Some of these options (see below)
allow to pass parameters, which can also be included in the
plan4res_settings.yml configuration file. Whenever a parameter is
present in the configuration file and via an option of p4r, the value
which will be used is the one in the option of p4r.

