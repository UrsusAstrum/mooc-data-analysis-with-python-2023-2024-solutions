#!/usr/bin/env python3

import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from matplotlib import pyplot as plt

def explained_variance():
    df = pd.read_csv("src/data.tsv", sep="\t")
    pca = PCA()
    pca.fit(df)
    return np.array(df.var(axis=0)), pca.explained_variance_

def main():
    v, ev = explained_variance()
    v_lst = " ".join([f"{i:.3f}" for i in v])
    ev_lst = " ".join([f"{i:.3f}" for i in ev])
    print(f"The variances are: {v_lst}")
    print(f"The explained variances after PCA are: {ev_lst}")

    cumsum = np.cumsum(ev)
    plt.plot(np.arange(1, len(cumsum) + 1), cumsum)
    plt.show()

if __name__ == "__main__":
    main()
