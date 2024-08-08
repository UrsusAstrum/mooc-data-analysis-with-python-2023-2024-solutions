#!/usr/bin/env python3

import scipy
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn import metrics
from sklearn.model_selection import train_test_split

def find_permutation(n_clusters, real_labels, labels):
    permutation=[]
    for i in range(n_clusters):
        idx = labels == i
        # Choose the most common label among data points in the cluster
        new_label = int(scipy.stats.mode(real_labels[idx])[0]) # Fixed error in their code
        permutation.append(new_label)
    return permutation

def plant_clustering():
    data = load_iris()
    X = data["data"]
    y = data["target"]
    model = KMeans(3, random_state=0)
    model.fit(X)

    permutation = find_permutation(3, y, model.labels_)
    real_labels = [permutation[label] for label in model.labels_]
    
    return metrics.accuracy_score(y, real_labels)

def main():
    print(plant_clustering())

if __name__ == "__main__":
    main()
