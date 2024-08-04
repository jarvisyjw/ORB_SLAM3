import numpy as np
import re
import math

def quat_to_rotationmatrix(qx,qy,qz,qw):
    q = np.array([qw, qx, qy, qz])
    q = q / np.linalg.norm(q)
    w, x, y, z = q
    return [
        [1-2*y**2-2*z**2, 2*x*y-2*z*w, 2*x*z+2*y*w],
        [2*x*y+2*z*w, 1-2*x**2-2*z**2, 2*y*z-2*x*w],
        [2*x*z-2*y*w, 2*y*z+2*x*w, 1-2*x**2-2*y**2]
    ]


def read_g2o_file(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    return lines

def write_kitti_file(data, out_file_path):
    with open(out_file_path, 'w') as f:
        for line in data:
            f.write("".join([str(elem) for elem in line]) + "\n")

def process_g2o_lines(lines):
    edge_pattern = re.compile(r'^VERTEX_SE2.*')
    edges = []
    i = 0
    for line in lines:
        if edge_pattern.match(line):
            parts = line.split()
            id =  int(parts[1])    
            x, y, theta = float(parts[2]), float(parts[3]), float(parts[4])
            rotation_matrix = quat_to_rotationmatrix(0,np.sin(theta/2),0,np.cos(theta/2))
            kitti_format_line = str(rotation_matrix[0][0]) +' '+ str(rotation_matrix[0][1]) +' '+ str(rotation_matrix[0][2]) +' '+str(x) + ' ' +str(rotation_matrix[1][0]) +' '+ str(rotation_matrix[1][1]) +' '+ str(rotation_matrix[1][2])+ ' '+ str(0)+' '+str(rotation_matrix[2][0]) +' '+ str(rotation_matrix[2][1]) +' '+ str(rotation_matrix[2][2])+" "+str(y)
            edges.append(kitti_format_line)
            i += 1

    return edges

# 输入g2o文件路径和输出kitti文件路径
def main(input_g2o_file, output_kitti_file):
    lines = read_g2o_file(input_g2o_file)
    kitti_data = process_g2o_lines(lines)
    write_kitti_file(kitti_data, output_kitti_file)

# 使用示例
input_g2o_file_path = './data/optimization_result/kitti_00_vo+lc.g2o'
output_kitti_file_path = './data/kitti/kitti_00_vo+lc.txt'
main(input_g2o_file_path, output_kitti_file_path)