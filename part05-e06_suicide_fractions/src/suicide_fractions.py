#!/usr/bin/env python3

import pandas as pd

def suicide_fractions():
    df = pd.read_csv("src/who_suicide_statistics.csv", index_col="country")
    df["mean"] = df["suicides_no"] / df["population"]
    groups = df.groupby("country")
    suicides = groups["mean"].mean()

    return suicides

def main():
    print(suicide_fractions())

if __name__ == "__main__":
    main()
