## Post-treating the results: the POSTTREAT module

The POSTTREAT module can be launched as follows:

> p4r POSTTREAT YourDataset -M simul
>
> p4r POSTTREAT YourDataset -M invest

POSTTREAT uses the python script PostTreatPlan4res.py (in
P4R_DIR/p4r-env/scripts/python/plan4res-scripts).

PostTreatPlan4res.py:

-   converts the outputs of SIM and CEM to more readable outputs (eg per
    region),

-   creates some additional and some synthetized output files (in
    results_simul/OUT or results_invest/OUT),

-   creates graphs (in results_simul /IMG or results_invest/IMG),

-   converts the outputs in IAMC format files (in results_simul /IAMC or
    results_invest/IAMC)

-   creates a latex report files (in results_simul /LATEX or
    results_invest/LATEX)

**Inputs**:

-   results of simulation in results_simul/ or in results_invest/

-   results of capacity expansion (if -M invest) in results_invest/

-   Bellman values in results_optim/

**Outputs**:

-   *[Detailed outputs]{.underline}*: Inputs and outputs of plan4res are
    converted in more readable files per regions:

```{=html}
<!-- -->
```
-   Power demand: Demand-\$region.csv,

-   Volumes in seasonal storage reservoirs:
    Volume-Reservoir-\$region.csv,

-   Generation schedules of all assets: Generation-\$region-\$i.csv

-   Marginal costs of the demand constraint:
    MarginalCostActivePowerDemand-\$region.csv, Histograms of the
    marginal costs: HistCmar-\$region.csv

-   Marginal costs of the interconnections:
    MarginalCost-\$reg2\$reg.csv,

-   Imports and exports per region: ImportExport-\$region-\$i.csv and
    ImportExport\$i.csv

```{=html}
<!-- -->
```
-   *[Synthetic outputs]{.underline}*: Synthetised results are produced:

```{=html}
<!-- -->
```
-   (initial) Installed Capacity: InitialInstalledCapacity.csv, (new)
    aggregated installed capacity: AggrInstalledCapacity.csv, (new)
    Installed Capacity: InstalledCapacity.csv and invested Capacity:
    InvestedCapacity.csv,

-   Non served energy per region: Slack-\$region.csv, and number of
    hours with non served energy: nbHoursSlack.csv,

-   Generation per technology: Generation.csv and
    Generation-\$region.csv , and per aggregated technologies:
    AggrGeneration.csv

-   Marginal costs: Histogram of scenarios of marginal costs:
    MonotoneCmar.csv, average on time of marginal costs:
    meanTimeCmar.csv, average on scenarios of marginal costs :
    meanScenCmar.csv,

-   Average imports and exports: MeanImportExport.csv and
    meanImportExport-\$region.csv

PostTreatPlan4res.py requires 4 configuration files:

-   settingsPostTreatPlan4res_XXX.yml (see section )

-   settings_format_XXX.yaml (see section 5.3.1.1)

-   settingsCreateInputPlan4res_XXX.yml (see section 5.2.2.1) which is
    also the main configuration file of CREATE.

-   VariablesDict.yml : contains the list of variables to retrieve and
    the correspondence between the plan4res and IAMC variable names (see
    section 5.2.2.3)

