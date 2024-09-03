from pathlib import Path
import numpy as np
from sklearn.metrics import average_precision_score, precision_recall_curve
from matplotlib import pyplot as plt

# max recall @ 100% precision
def max_recall(precision: np.ndarray, recall: np.ndarray):
    recall_idx = np.argmax(recall)
    idx = np.where(precision == 1.0)
    max_recall = np.max(recall[idx])
    # logger.debug(f'max recall{max_recall}')
    recall_idx = np.array(np.where(recall == max_recall)).reshape(-1)
    recall_idx = recall_idx[precision[recall_idx]==1.0]
    # logger.debug(f'recall_idx {recall_idx}')
    r_precision, r_recall = float(np.squeeze(precision[recall_idx])), float(np.squeeze(recall[recall_idx]))
    # logger.debug(f'precision: {r_precision}, recall: {r_recall}')
    return r_precision, r_recall

# plot precision recall curve
def plot_pr_curve(recall: np.ndarray, precision: np.ndarray, average_precision, method = 'SP+SG', exp_name = 'test', c = None):
    # calculate max f2 score, and max recall
    f_score = 2 * (precision * recall) / (precision + recall)
    f_idx = np.argmax(f_score)
    f_precision, f_recall = np.squeeze(precision[f_idx]), np.squeeze(recall[f_idx])
    r_precision, r_recall = max_recall(precision, recall)
    plt.plot(recall, precision, label="{} (AP={:.5f})".format(method, average_precision))
    plt.vlines(r_recall, np.min(precision), r_precision, colors='green', linestyles='dashed')
    plt.vlines(f_recall, np.min(precision), f_precision, colors='red', linestyles='dashed')
    plt.hlines(f_precision, np.min(recall), f_recall, colors='red', linestyles='dashed')
    plt.hlines(r_precision, np.min(recall), r_recall, colors='green', linestyles='dashed')
    plt.xlim(0, None)
    plt.ylim(np.min(precision), None)
    plt.text(f_recall + 0.005, f_precision + 0.005, '[{:.5f}, {:.5f}]'.format(f_recall, f_precision))
    plt.text(r_recall + 0.005, r_precision + 0.005, '[{:.5f}, {:.5f}]'.format(r_recall, r_precision))
    plt.scatter(f_recall, f_precision, marker='o', color='red', label='Max F score')
    plt.scatter(r_recall, r_precision, marker='o', color='green', label='Max Recall')
    plt.xlabel("Recall")
    plt.ylabel("Precision")
    plt.legend()
    plt.title("Precision-Recall Curves for {}".format(exp_name))

def parse_retrieval(results: str) -> list:
    """
    Parse the retrieval results into a list of tuples.
    """
    
    dtype = np.dtype([('query', np.int32), ('reference', np.int32), ('score', np.float16), ('num_matches', np.int32), ('inlier', np.int32), ('gt', np.int32)])
    rets = np.loadtxt(results, dtype=dtype)
    scores = np.array([ret['score'] for ret in rets], dtype=np.float64)
    num_matches = np.array([ret['num_matches'] for ret in rets], dtype=np.int32)
    inliers = np.array([ret['inlier'] for ret in rets], dtype=np.int32)
    labels = np.array([ret['gt'] for ret in rets], dtype=np.int32)
    inliers_norm = inliers / max(num_matches)
    
    return scores, inliers_norm, labels


def eval(scores, labels, method, exp_name):
    """
    Evaluate the retrieval results.
    """
    average_precision = average_precision_score(labels, scores)
    precision, recall, TH = precision_recall_curve(labels, scores)
    precision_r, recall_max = max_recall(precision, recall)
    plot_pr_curve(recall, precision, average_precision, method, exp_name)
    print(f"Average Precision: {average_precision} \n")
    print(f"Max Recall @ 100% Precision: {recall_max} \n")
    return average_precision, recall_max


def plot_pr_curves(recall: list, precision: list, method = 'test', color='green'):
        r_precision, r_recall = max_recall(precision, recall)
        plt.plot(recall, precision, label="{} (MR={:.1f})".format(f'{method}', r_recall*100), color=color)
        plt.ylim(np.min(precision), 1.005)
        plt.xlim(0, None)
        plt.xlabel("Recall")
        plt.ylabel("Precision")
        plt.legend()
        # legend position
        plt.legend(loc='center left', bbox_to_anchor=(0, 0.3))
    

def plot(scores, labels, methods, exp_name):
    """
    Plot the precision-recall curves.
    """
    plt.figure(figsize=(6.8, 5))
    plt.rcParams['text.usetex'] = True
    # font times new roman
    # font bold
    plt.rcParams['font.weight'] = 'bold'
    plt.rcParams['font.family'] = 'Arial'
    
    colors = ['b', 'c']

    for score, method, c in zip(scores, methods, colors):
        average_precision = average_precision_score(labels, score)
        precision, recall, TH = precision_recall_curve(labels, score)
        precision_r, recall_max = max_recall(precision, recall)
        plot_pr_curves(recall, precision, method, c)
        print(f"Average Precision: {average_precision} \n")
        print(f"Max Recall @ 100% Precision: {recall_max} \n")
        
    plt.title("Precision-Recall Curves for {}".format(exp_name))


if __name__ == "__main__":
    # parse retrieval results
    results = Path("data/unitysim/unitysim_01/DBow2loop_gt.txt")
    dbow, gv, labels = parse_retrieval(results)
    
    # evaluate the retrieval results
    scores = [dbow, gv]
    methods = ["DBoW2", "GV"]
    exp_name = "UnitySim01"
    plot(scores, labels, methods, exp_name)
    plt.show()
    
    
    
