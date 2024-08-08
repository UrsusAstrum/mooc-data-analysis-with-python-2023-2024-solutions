#!/usr/bin/env python3

import pandas as pd
import numpy as np

def last_week():
    df = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")
    df = df.replace(["New", "Re"], value=None)
    df[["Pos", "LW"]] = df[["Pos", "LW"]].astype('float')
    df = df.dropna()
    mask = (df['Peak Pos'] == df['Pos']) & (df['Pos'] < df['LW'])
    df.loc[mask, 'Peak Pos'] = np.nan
    df = df.sort_values(by=["LW"])
    df.index = df["LW"]
    df = df.reindex(range(1,41))
    df['Pos'] = df.index
    df['LW'] = np.nan
    df["WoC"] -= 1
    return df

def main():
    df = last_week()
    print("Shape: {}, {}".format(*df.shape))
    print("dtypes:", df.dtypes)
    print(df)


if __name__ == "__main__":
    main()
