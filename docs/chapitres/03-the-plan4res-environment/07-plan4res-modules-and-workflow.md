# Plan4res modules and workflow

plan4res is composed of the modules listed below. The workflow between the modules is illustrated in Figure 4.

![Une image contenant texte, Police, diagramme, capture d’écran
Description générée automatiquement](media/media/image3.jpg)

Figure 4: plan4res workflow

- CREATE: creates a plan4res CSV dataset out of a scenario in IAMC format (in IAMC/) and hourly timeseries

- FORMAT: creates a plan4res NetCDF dataset out of the plan4res CSV input data and the hourly timeseries

- SSV: solves the Seasonal Storage Valuation problem. Uses NetCDF files in nc4_optim and computes Bellman Values, stores the results in results_optim

- SSV: solves the Seasonal Storage Valuation problem. Uses NetCDF files in nc4_optim and computes Bellman Values, stores the results in results_optim

- SIM: solves the simulation problem. Uses NetCDF files in nc4_simul and computes schedules of all assets and marginal costs, stores the results in results_simul

- CEM: solves the capacity expansion problem. Uses NetCDF files in nc4_invest and computes new investments, as well as the schedules of all assets and marginal costs for the new power system, including invested assets, stores the results in results_invest