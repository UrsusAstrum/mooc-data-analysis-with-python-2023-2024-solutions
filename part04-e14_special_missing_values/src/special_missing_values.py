#!/usr/bin/env python3

import pandas as pd
import numpy as np

def special_missing_values():
    df = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")
    df = df.replace(["New", "Re"], value=None)
    df[["Pos", "LW"]] = df[["Pos", "LW"]].astype('float')    
    df = df[df["Pos"] > df["LW"]]
    
    return df

def main():
    print(special_missing_values().head())

if __name__ == "__main__":
    main()
