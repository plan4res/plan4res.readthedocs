# plan4res IAMC input data

The IAMC input data should be composed of one csv file whose name should be Dataset.xlsx. This file can be an output of the model GEneSYS-MOD. It will be used by the plan4res CREATE module to create plan4res csv input data files. It is also possible to adapt the configuration file of CREATE in order to use more than one IAMC file for retrieving the different variables (take some variables from one IAMC file, and other variables from another IAMC file).

These files have to follow the IAMC data format, described in the deliverable D4.2Available at [https://doi.org/10.5281/zenodo.5521098](https://doi.org/10.5281/zenodo.5521098) (data exchange format and template) of open ENTRANCE, using the variables and regions defined in the open ENTRANCE nomenclature[openENTRANCE/openentrance: Definitions of common terms (variables, regions, etc.) for the openENTRANCE project](https://github.com/openENTRANCE/openentrance).

![](media/media/image6.png)

Table 1: example of IAMC input data used by script CreateInputPlan4res.py to create the plan4res files