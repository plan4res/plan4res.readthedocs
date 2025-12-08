### Additional columns for dealing with Investments (CEM)

To run the Capacity Expansion Model (CEM), 4 columns need to be added to
the files corresponding to assets in which one wants to invest (see
below), ie to the files describing the generation units (apart from
Seasonal Storages) as well as to the file describing the interconnection
(see ):

Table 12: additional columns for capacity expansion

  -----------------------------------------------------------------------------------------------------------------------------
  **Zone**    **Name**       **....**   **InvestmentCost**   **DecommissionCost**   **MaxAddedCapacity**   **MaxRetCapacity**
  ----------- -------------- ---------- -------------------- ---------------------- ---------------------- --------------------
  DolAmroth   Biomass\|w/o              1980000              100                    5000                   0
              CCS                                                                                          

  RoGonDor    Biomass\|w/o              1980000              100                    4000                   0
              CCS                                                                                          

  Harad       Biomass\|w/o              1980000              100                    500                    0
              CCS                                                                                          

  DolAmroth   Coal\|Hard                1082250              100                    0                      2000
              coal\|w/o CCS                                                                                
  -----------------------------------------------------------------------------------------------------------------------------

-   **MaxAddedCapacity**: this is the maximum capacity that may be
    added, in MW.

-   **MaxRetCapacity**: this is the maximum capacity that may be
    decommissioned, in MW.

-   **InvestmentCost**: this is the cost for investing into the given
    capacity in the given zone, in €/MW. Note that these are yearly
    costs, computed as Capital Cost / LifeTime (in years) + Fixed Cost.

-   **DecommissionCost**: this is the cost for decommissioning the given
    capacity in the given zone, in €/MW.

Costs are not discounted.

These columns may then be added to the following files:

-   IN_Interconnections.csv

-   TU_ThermalUnits.csv

-   STS_ShortTermStorage.csv

-   RES_RenewableUnits.csv

Note that investment in new seasonal storages is not available at
present.

