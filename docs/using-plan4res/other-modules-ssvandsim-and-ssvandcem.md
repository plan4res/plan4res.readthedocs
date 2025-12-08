### Other modules: SSVandSIM and SSVandCEM

These modules include complete workflows.

p4r SSVandSIM YourDataset does the following:

-   If used with option -C: p4r CREATE YourDataset

-   p4r FORMAT YourDataset -M optim

-   p4r SSV YourDataset

-   p4r FORMAT YourDataset -M simul

-   p4r SIM YourDataset

-   p4r POSTTREAT YourDataset

p4r SSVandCEM YourDataset does the following:

-   If used with option -C: p4r CREATE YourDataset -M invest

-   p4r FORMAT YourDataset -M optim -m invest

-   p4r SSV YourDataset -M invest

-   p4r FORMAT YourDataset -M invest

-   p4r CEM YourDataset

-   p4r POSTTREAT YourDataset -M invest

