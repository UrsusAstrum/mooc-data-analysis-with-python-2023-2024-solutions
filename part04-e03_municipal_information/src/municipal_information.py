#!/usr/bin/env python3

import pandas as pd

def main():
    data = pd.read_csv("src/municipal.tsv", sep="\t")
    print(f"Shape: {data.shape[0]},{data.shape[1]}")
    print("Columns:")
    for i in data.columns:
        print(i)


if __name__ == "__main__":
    main()
