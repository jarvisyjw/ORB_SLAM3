from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
import numpy as np
import matplotlib.pyplot as plt

def data_load(filename):
    res_list = []
    y_test = []

    with open(filename,'r') as f:
        for line in f:
            res_val = float(line.split()[1])
            res_index = int(line.split()[0])
            res_list.append(res_val)
            if res_index < 60:
                y_test.append(1)
            else:
                y_test.append(0)
    return res_list,y_test


def res2prob(res_list):
    res_list = np.array(res_list)
    probs = 1/res_list
    min_val = min(probs)
    max_val = max(probs)
    normalized = (probs - min_val)/(max_val - min_val) 
    return  normalized

def rp_curve_plot(probs, y_test,data_name):
    print("max:",min(probs),"min:",max(probs))
    thresholds = np.arange(np.min(probs),np.max(probs),0.0001)

    print("threshold",thresholds)
    print("probs:",probs)
    precisions = []
    recalls = []

    for threshold in thresholds:
        y_predict = np.array(probs >= threshold, dtype = 'int')
        pre = precision_score(y_test, y_predict)
        recall = recall_score(y_test, y_predict)
        precisions.append(pre)
        recalls.append(recall)
        print("threshold:",threshold,"\ny_precict",y_predict,"\npre and recall:",pre,recall,"\n-----------------")

    # print("pre:",precisions,"\nrecall:",recalls)
    
    plt.figure(figsize=(6.8, 5))
    plt.plot(recalls,precisions)
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.title(f"Precision-Recall Curves for {data_name}")
    plt.savefig(f"./data/plot/{data_name}_PR_curves.png", bbox_inches='tight', dpi = 300)

    plt.show()
   


if __name__ == "__main__":
    # data_name = "ais2klinik"
    data_name = "kitti_02"
    # data_name = "MIT"
    # data_name = "manhattan"
    # data_name = "sphere2500"


    res_list , y_test = data_load(f"./data/rp_data/{data_name}_val.txt")
    #样本数量
    probs = res2prob(res_list)
    rp_curve_plot(probs, y_test,data_name)