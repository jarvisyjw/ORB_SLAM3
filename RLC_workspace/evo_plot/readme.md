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


数据命名：
kitti_00_vo.txt 纯vo
kitti_00_vo+fp  纯vo+false positive
kitti_00_vo+lc  vo+loop closure
kitti_00_vo+lc+hfp vo+loop closure + huge false positive
kitti_00_vo+lc+mfp vo+loop closure + mild false positive
kitti_00_vo+lc+sfp vo+loop closure + slight false positive
kitti_00_vo+nlc vo+n 个loop closure 


- KITTI_00_VO.txt Visual Odometry Only
- KITTI_00_VO_FP.txt Visual Odometry + False Positives
- KITTI_00_VO_LC.txt Visual Odometry + Loop Closure
- KITTI_00_VO_LC_FP_High.txt Visual Odometry + Loop Closure + High False Positives
- KITTI_00_VO_LC_FP_Medium.txt Visual Odometry + Loop Closure + Medium False Positives
- KITTI_00_VO_LC_FP_Low.txt Visual Odometry + Loop Closure + Low False Positives
- KITTI_00_VO_NLC.txt Visual Odometry + N Loop Closures

--usage
evo_traj kitti ./data/kitti/kiiti_00.txt -p

--usage 
TP:  
evo_traj kitti ./data/kitti/KITTI_00_VO_LC.txt ./data/kitti/KITTI_00_VO.txt --ref=./data/kitti/KITTI_00_gt.txt -p -a --plot_mode=xz

FP:  
evo_traj kitti ./data/kitti/KITTI_00_VO_LC_FP_High.txt ./data/kitti/KITTI_00_VO_LC_FP_Medium.txt ./data/kitti/KITTI_00_VO_LC_FP_Low.txt  ./data/kitti/KITTI_00_VO_LC.txt  ./data/kitti/KITTI_00_VO.txt  --ref=./data/kitti/KITTI_00_gt.txt -p -a --plot_mode=xz

FN:
evo_traj kitti ./data/kitti/KITTI_00_VO_NLC.txt ./data/kitti/KITTI_00_VO.txt  --ref=./data/kitti/KITTI_00_gt.txt -p -a --plot_mode=xz

TN:
evo_traj kitti ./data/kitti/KITTI_00_VO_FP.txt  ./data/kitti/KITTI_00_VO.txt --ref=./data/kitti/KITTI_00_gt.txt -p -a --plot_mode=xz


--save_results results/SPTAM.zip
evo_res results/*.zip -p --save_table results/table.csv
evo_ape kitti ./data/kitti/kitti_00_vo+lc+sfp.txt ./data/kitti/KITTI_00_gt.txt  -va --plot --plot_mode=xz --plot_colormap_max -11
evo_ape kitti ./data/kitti/kitti_00_vo+lc+mfp.txt ./data/kitti/KITTI_00_gt.txt  -va --plot --plot_mode=xz
evo_ape kitti ./data/kitti/kitti_00_vo+lc+hfp.txt ./data/kitti/KITTI_00_gt.txt  -va --plot --plot_mode=xz
evo_ape kitti ./data/kitti/kitti_00_vo+lc.txt ./data/kitti/KITTI_00_gt.txt  -va --plot --plot_mode=xz


