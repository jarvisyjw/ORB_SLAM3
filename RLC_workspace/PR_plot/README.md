This is used to plot the PR curve of the our binairy classification algorithm 

1. modify_edge.py: used to generated samples of different datasets by modifying the loop closure edges of original dataset.

2. pgo_g2o.py: used to sovle the PGO by g2o-py, and gernerate the converge residual of g2o samples.
ex: python pgo_g2o 2>./data/output_data/{data_name}_output.txt

3. test.py: used to transfer ./data/output_data/{data_name}_output.txt to ./data/rp_data/{data_name}_val.txt

4. pr_plot: used to plot the PR curve with inputting the ./data/rp_data/{data_name}_val.txt
