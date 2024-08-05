1. usage --重定向将优化的残差结果输出到result_optimizer.txt
./pose_graph_g2o_SE3 ./data/smallGrid3D.g2o 2>result_optimizer.txt

2. --画出优化结果
./plot_convergence.py