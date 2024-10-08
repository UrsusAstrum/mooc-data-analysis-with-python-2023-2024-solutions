#!/usr/bin/env python3

import pandas as pd

def swedish_and_foreigners():
    df = pd.read_csv("src/municipal.tsv", sep="\t", index_col="Region 2018")
    df = df["Akaa": "Äänekoski"]
    df = df[(df["Share of Swedish-speakers of the population, %"] > 5) & (df["Share of foreign citizens of the population, %"] > 5)]
    df = df[["Population", "Share of Swedish-speakers of the population, %", "Share of foreign citizens of the population, %"]]

    return df


def main():
    print(swedish_and_foreigners().head())

if __name__ == "__main__":
    main()
