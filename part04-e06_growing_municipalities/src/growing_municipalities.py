#!/usr/bin/env python3

import pandas as pd
import numpy as np

def growing_municipalities(df):
    total = df.shape[0]
    growing = np.sum(df["Population change from the previous year, %"] > 0)
    return growing / total

def main():
    df = pd.read_csv("src/municipal.tsv", sep="\t", index_col="Region 2018")
    df["Akaa":"Äänekoski"]
    print(f"Proportion of growing municipalities: {growing_municipalities(df):.1f}%")

if __name__ == "__main__":
    main()
