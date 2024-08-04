import re
import matplotlib.pyplot as plt
import math
import numpy as np


def parse_file(file_path):
    iterations = []
    chi2_values = []

    # 定义正则表达式模式
    pattern = r"iteration=\s(\d+)\s+chi2=\s(\d*\.\d+)"

    with open(file_path, 'r') as file:
        for line in file:
            match = re.search(pattern, line)
            if match:
                iteration = int(match.group(1))
                chi2 = float(match.group(2))
                iterations.append(iteration)
                chi2_values.append(chi2)

    return iterations, chi2_values



def main():
    # 文件路径
    file_path_0 = 'result_optimizer.txt'
    iterations_0, chi2_values_0 = parse_file(file_path_0)
    chi2_values_log_0 = np.log(chi2_values_0)
    print("Iterations:", iterations_0)
    print("Chi2 values:", chi2_values_0)
    
    file_path_1 = 'result_optimizer.txt'
    iterations_1, chi2_values_1 = parse_file(file_path_1)
    chi2_values_log_1 = np.log(chi2_values_1)

    file_path_2 = 'result_optimizer.txt'
    iterations_2, chi2_values_2 = parse_file(file_path_2)
    chi2_values_log_2 = np.log(chi2_values_2)

    file_path_3 = 'result_optimizer.txt'
    iterations_3, chi2_values_3 = parse_file(file_path_3)
    chi2_values_log_3 = np.log(chi2_values_3)



    # 创建绘图
    plt.figure(figsize=(10, 6))
    plt.plot(iterations_0, chi2_values_0,marker='o', linestyle='-', color='r',label = 'correct loopclosure')
    plt.plot(iterations_1, chi2_values_1,marker='o', linestyle='-', color='b',label = 'wrong loopclosure-1')
    plt.plot(iterations_2, chi2_values_2,marker='s', linestyle='-', color='b', label = 'wrong loopclosure-2')
    plt.plot(iterations_3, chi2_values_3,marker='d', linestyle='-', color='b', label = 'wrong loopclosure-3')
    plt.xlabel('Iteration', fontsize=14)
    plt.ylabel('Chi2', fontsize=14)
    plt.title('Chi2 with iteration in xxx dataset', fontsize=16)
    plt.xlim(0,20)
    plt.grid(True)
    plt.legend()
    plt.savefig('./figures/xxx.png')
    plt.show()

    #绘制log图
    plt.figure(figsize=(10, 6))
    plt.plot(iterations_0, chi2_values_log_0,marker='o', linestyle='-', color='r',label = 'correct loopclosure')
    plt.plot(iterations_1, chi2_values_log_1,marker='o', linestyle='-', color='b',label = 'wrong loopclosure-1')
    plt.plot(iterations_2, chi2_values_log_2,marker='s', linestyle='-', color='b', label = 'wrong loopclosure-2')
    plt.plot(iterations_3, chi2_values_log_3,marker='d', linestyle='-', color='b', label = 'wrong loopclosure-3')
    plt.xlabel('Iteration', fontsize=14)
    plt.ylabel('Chi2', fontsize=14)
    plt.title('Log(Chi2) with iteration in xxx dataset', fontsize=16)
    plt.xlim(0,20)
    plt.grid(True)
    plt.legend()
    plt.savefig('./figures/xxx_log.png')
    plt.show()
 

# 确保脚本直接运行时调用main函数
if __name__ == "__main__":
    main()