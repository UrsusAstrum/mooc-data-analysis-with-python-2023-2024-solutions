#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt

days = dict(zip("ma ti ke to pe la su".split(), "Mon Tue Wed Thu Fri Sat Sun".split()))
months = dict(zip("tammi helmi maalis huhti touko kesä heinä elo syys loka marras joulu".split(), range(1, 13)))
 
def split_date(df):
    d = df["Päivämäärä"].str.split(expand=True)
    d.columns = ["Weekday", "Day", "Month", "Year", "Hour"]
 
    hourmin = d["Hour"].str.split(":", expand=True)
    d["Hour"] = hourmin.iloc[:, 0]
 
    d["Weekday"] = d["Weekday"].map(days)
    d["Month"] = d["Month"].map(months)
    
    d = d.astype({"Weekday": object, "Day": int, "Month": int, "Year": int, "Hour": int})
    return d
 
def split_date_continues():
    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
    df = df.dropna(axis=0, how="all").dropna(axis=1, how="all")
    d = split_date(df)
    df = df.drop("Päivämäärä", axis=1)
    result = pd.concat([d, df], axis=1)
    return result

def bicycle_timeseries():
    df = split_date_continues()
    df["Date"] = pd.to_datetime(df[["Year", "Month", "Day", "Hour"]])
    df = df.set_index("Date")
    df = df.drop(columns=["Day", "Month", "Year", "Hour"])
    return df

def commute():
    df = bicycle_timeseries()["2017-8-01": "2017-08-31"]
    tot = df.groupby("Weekday").sum()
    tot.index = [1, 2, 3, 4, 5, 6, 7]

    return tot

    
def main():
    df = commute()
    df.plot()
    plt.show()



if __name__ == "__main__":
    main()
