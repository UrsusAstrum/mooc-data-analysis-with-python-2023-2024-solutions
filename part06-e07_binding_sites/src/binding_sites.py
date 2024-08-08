#!/usr/bin/env python3
""" Note that this exercise will fail some tests due to the 
lack of an affinity parameter (replaced by metric) 
for the AgglomerateClustering model.
"""

import pandas as pd
import numpy as np
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import accuracy_score
from sklearn.metrics import pairwise_distances
import scipy
from matplotlib import pyplot as plt

import seaborn as sns
sns.set(color_codes=True)
import scipy.spatial as sp
import scipy.cluster.hierarchy as hc

def find_permutation(n_clusters, real_labels, labels):
    permutation=[]
    for i in range(n_clusters):
        idx = labels == i
        # Choose the most common label among data points in the cluster
        new_label = int(scipy.stats.mode(real_labels[idx])[0]) # Fixed error in their code
        permutation.append(new_label)
    return permutation

def toint(x):
    nucleotides = ["A", "C", "G", "T"]

    return nucleotides.index(x)

def get_features_and_labels(filename):
    df = pd.read_csv(filename, sep="\t")
    feature_matrix = np.stack(np.array(df["X"].map(lambda x : np.array([toint(i) for i in x]))))
    feature_labels = np.array(df["y"])
    return (feature_matrix, feature_labels)

def plot(distances, method='average', affinity='euclidean'):
    mylinkage = hc.linkage(sp.distance.squareform(distances), method=method)
    g=sns.clustermap(distances, row_linkage=mylinkage, col_linkage=mylinkage)
    g.fig.suptitle(f"Hierarchical clustering using {method} linkage and {affinity} affinity")
    plt.show()

def cluster_euclidean(filename):
    X, y = get_features_and_labels(filename)
    model = AgglomerativeClustering(metric="euclidean", linkage="average", n_clusters=2) # Affinity parameter invalid.
    y_pred = model.fit_predict(X)
    permutation = find_permutation(2, y, y_pred)
    real_labels = [permutation[label] for label in y_pred]

    return accuracy_score(y, real_labels)

def cluster_hamming(filename):
    X, y = get_features_and_labels(filename)
    distance_matrix = pairwise_distances(X, metric="hamming")
    model = AgglomerativeClustering(metric="precomputed", linkage="average", n_clusters=2) # Affinity parameter invalid.
    y_pred = model.fit_predict(distance_matrix)
    permutation = find_permutation(2, y, y_pred)
    real_labels = [permutation[label] for label in y_pred]
    return accuracy_score(y, real_labels)



def main():
    print("Accuracy score with Euclidean affinity is", cluster_euclidean("src/data.seq"))
    print("Accuracy score with Hamming affinity is", cluster_hamming("src/data.seq"))

if __name__ == "__main__":
    main()
