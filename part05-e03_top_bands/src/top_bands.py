#!/usr/bin/env python3

import pandas as pd

def top_bands():
    bands = pd.read_csv("src/bands.tsv", sep="\t")
    charts = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")
    charts["Artist"] = charts["Artist"].str.title()
    bands["Band"] = bands["Band"].str.title()
    return pd.merge(bands, charts, left_on="Band", right_on="Artist")

def main():
    print(top_bands().head())

if __name__ == "__main__":
    main()
