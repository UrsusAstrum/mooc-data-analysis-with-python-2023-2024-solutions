#!/usr/bin/env python3

import pandas as pd

def best_record_company():
    df = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")
    groups = df.groupby("Publisher")
    best = groups["WoC"].sum().sort_values().index[-1]
    return df[df["Publisher"] == best]

def main():
    print(best_record_company())
    

if __name__ == "__main__":
    main()
