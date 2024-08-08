#!/usr/bin/env python3

import pandas as pd
import numpy as np


def split_date():
    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
    df = df.dropna(axis=0, how="all")
    df = df.dropna(axis=1, how="all")

    df = df["Päivämäärä"].str.split(expand=True)
    df.columns = ["Weekday", "Day", "Month", "Year", "Hour"]
    df = df.replace({"ma": "Mon", "ti": "Tue", "ke": "Wed", "to": "Thu", "pe": "Fri", "la": "Sat", "su": "Sun"})
    df = df.replace({"tammi" : 1, "helmi" : 2, "maalis" : 3, "huhti" : 4, "touko" : 5, "kesä" : 6, "heinä" : 7, "elo" : 8, "syys" : 9, "loka" : 10, "marras" : 11, "joulu" : 12})
    df["Hour"] = df["Hour"].str.replace(r"\d+:", "", regex=True)
    df[["Day", "Year", "Hour"]] = df[["Day", "Year", "Hour"]].astype(int)

    return df

def main():
    print(split_date().head())
       
if __name__ == "__main__":
    main()
