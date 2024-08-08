#!/usr/bin/env python3

import pandas as pd
import numpy as np


def cleaning_data():
    df = pd.read_csv("src/presidents.tsv", sep="\t")

    # President

    df["President"] = df["President"].str.replace(r",", " ", regex=True)
    df["President"] = df["President"].str.title()
    df.at[2, "President"] = "George Bush"
    df.at[3, "President"] = "Bill Clinton"

    df["President"] = df["President"].astype(object)

    # Start

    df.at[0, "Start"] = 2017
    df["Start"] = df["Start"].astype(int)

    # Last

    df.at[0, "Last"] = np.nan
    df["Last"] = df["Last"].astype(float)

    # Seasons

    df.at[3, "Seasons"] = 2
    df["Seasons"] = df["Seasons"].astype(int)

    # Vice-president

    df["Vice-president"] = df["Vice-president"].str.replace(r",", " ", regex=True)
    df["Vice-president"] = df["Vice-president"].str.title()
    df.at[2, "Vice-president"] = "Dick Cheney"
    df.at[3, "Vice-president"] = "Al Gore"

    return df


def main():
    print(cleaning_data())

if __name__ == "__main__":
    main()
