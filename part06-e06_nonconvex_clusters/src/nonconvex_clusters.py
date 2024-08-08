#!/usr/bin/env python3

import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.metrics import accuracy_score
from collections import Counter
import scipy

def find_permutation(n_clusters, real_labels, labels):

    if n_clusters != len(set(real_labels)):
        return None
    
    outlier_mask = labels[labels != -1]
    labels = labels[outlier_mask]
    real_labels = real_labels[outlier_mask]

    permutation=[]
    for i in range(n_clusters):
        idx = labels == i
        # Choose the most common label among data points in the cluster
        new_label = int(scipy.stats.mode(real_labels[idx])[0]) # Fixed error in their code
        permutation.append(new_label)
    return permutation

def nonconvex_clusters():

    df = pd.read_csv("src/data.tsv", sep="\t")
    eps_arr = np.arange(0.05, 0.2, 0.05)

    res = pd.DataFrame()
    res["eps"] = eps_arr

    n_clusters = []
    n_outliers = []
    score = []

    for eps in eps_arr:
        model = DBSCAN(eps=eps)
        model.fit(df[["X1", "X2"]])
        target = df["y"]
        n_outliers.append(Counter(model.labels_)[-1])
        n_clusters.append(len(set(model.labels_)) - (1 if -1 in model.labels_ else 0))
        permutation = find_permutation(n_clusters[-1], target, model.labels_)
        if permutation == None:
            score.append(np.nan)
        else:
            outlier_mask = model.labels_[model.labels_ != -1]
            labels = model.labels_[outlier_mask]
            real_labels = target[outlier_mask]
            score.append(accuracy_score(real_labels, [permutation[label] for label in labels]))

    res["Score"] = score
    res["Clusters"] = n_clusters
    res["Outliers"] = n_outliers

    res = res.astype(float)

    return res

def main():
    print(nonconvex_clusters())

if __name__ == "__main__":
    main()
