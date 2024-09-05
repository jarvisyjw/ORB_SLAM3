这是用来画出g2o优化的残差结果随着迭代次数的收敛的图， 如./figures所示
8个datasets的收敛结果图已经在figures-2.pptx


1. usage --重定向将优化的残差结果输出到result_optimizer.txt
./pose_graph_g2o_SE3 ./data/smallGrid3D.g2o 2>result_optimizer.txt

2. --画出优化结果
./plot_convergence.py