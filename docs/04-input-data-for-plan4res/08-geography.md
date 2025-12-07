# Geography

Each dataset is linked to a geographical area that may be partitioned. Different partitions may be used for dealing with different levels of constraints or computations. The constraints related to the power demand (which must be equal to the power generation) are applied at the lowest level of the partition, which is called Nodes. It can correspond to countries, or to sub-country regions. Some constraints (namely system services constraints) may apply to different partitions (e.g. to group of countries).

The Figure 5 below illustrates this:

- In blue: the lowest level of partitions (level1), ie the Nodes; In this case there are 7 nodes in level1.

- In green: a second level of partition (level2), with 4 clusters of nodes (named here BE, FR1, FR2 and ES). Note that each level1 node belongs to a unique level2 cluster.

- In red and orange, there are 2 different partitions for the third level , grouping together clusters of level2. The orange partition is composed of 2 clusters (North and South), themselves composed of green clusters defined at level 2. The red partition is composed of 3 clusters (BE, FR, ES), themselves composed of green clusters defined at level 2.

- In black, the biggest partition has a unique cluster.

![](media/media/image4.png)

Figure 5: geographical partitions