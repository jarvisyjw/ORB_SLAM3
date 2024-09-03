# https://github.com/RainerKuemmerle/g2o/blob/master/g2o/examples/simple_optimize/simple_optimize.cpp

import numpy as np
import g2o 
import os



def main(input_file, iterations):
    solver = g2o.BlockSolverX(g2o.LinearSolverCholmodX())
    # solver = g2o.BlockSolverSE3(g2o.LinearSolverEigenSE3())
    solver = g2o.OptimizationAlgorithmLevenberg(solver)

    optimizer = g2o.SparseOptimizer()
    optimizer.set_verbose(True)
    optimizer.set_algorithm(solver)

    optimizer.load(input_file)
    print('num vertices:', len(optimizer.vertices()))
    print('num edges:', len(optimizer.edges()), end='\n\n')

    optimizer.initialize_optimization()
    optimizer.optimize(iterations)


if __name__ == '__main__':
    # data_name = "manhattan"
    # data_name = "MIT"
    # data_name = "ais2klinik"
    # data_name = "kitti_00"
    data_name = "sphere2500"



    n = 101
    iterations = 20

    for i in range(n):
        input_file = f"./data/{data_name}_samples/{i}.g2o"
        main(input_file,iterations)
