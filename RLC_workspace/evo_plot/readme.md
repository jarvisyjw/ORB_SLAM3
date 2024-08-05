.g2o_SE2数据格式类型
EDGE_SE2 id1 id2 x y theta info_1 info_2 info_3 info_4 info_5 info_6

对应四元数【 0 0 sin(theta/2) cos(theta/2)】


evo kitti数据格式
4*4同质位姿矩阵的前三行
a b c d
e f g h
i j k l 
0 0 0 1

a b c d e f g h i j k l

cos(z) -sin(z) 0 x
sin(z) cos(z)  0 y
0 0 1 0
0 0 0 1

--usage
evo_traj kitti ./data/kitti/kiiti_00.txt -p

--usage 
TP:  
evo_traj kitti ./data/kitti/kitti_00_vo+lc.txt ./data/kitti/kitti_00_vo.txt --ref=./data/kitti/KITTI_00_ORB.txt -p --plot_mode=xz
FP:  
evo_traj kitti ./data/kitti/kitti_00_vo+lc.txt ./data/kitti/kitti_00_vo.txt --ref=./data/kitti/kitti_00_vo+lc.txt -p --plot_mode=xy
FP:  
evo_traj kitti ./data/kitti/kitti_00_vo+lc.txt ./data/kitti/kitti_00_vo.txt --ref=./data/kitti/kitti_00_vo+lc.txt -p --plot_mode=xy
FP: 
evo_traj kitti ./data/kitti/kitti_00_vo+lc.txt ./data/kitti/kitti_00_vo.txt --ref=./data/kitti/kitti_00_vo+lc.txt -p --plot_mode=xy

--usage 
TP:  
evo_traj kitti ./data/kitti/kitti_00_vo+lc.txt ./data/kitti/kitti_00_vo.txt  --ref=./data/kitti/kitti_00_vo+lc.txt -p --plot_mode=xz
FP:  
evo_traj kitti ./data/kitti/kitti_00_vo+fp.txt ./data/kitti/kitti_00_vo.txt  --ref=./data/kitti/kitti_00_vo+lc.txt -p --plot_mode=xz
FN:
evo_traj kitti ./data/kitti/kitti_00_vo+nlc.txt ./data/kitti/kitti_00_vo.txt  --ref=./data/kitti/kitti_00_vo+lc.txt -p --plot_mode=xz
TN:
evo_traj kitti ./data/kitti/kitti_00_vo+lc+hfp.txt ./data/kitti/kitti_00_vo.txt  --ref=./data/kitti/kitti_00_vo+lc.txt -p --plot_mode=xz
evo_traj kitti ./data/kitti/kitti_00_vo+lc+sfp.txt ./data/kitti/kitti_00_vo.txt  --ref=./data/kitti/kitti_00_vo+lc.txt -p --plot_mode=xz
evo_traj kitti ./data/kitti/kitti_00_vo+lc+mfp.txt ./data/kitti/kitti_00_vo.txt  --ref=./data/kitti/kitti_00_vo+lc.txt -p --plot_mode=xz
