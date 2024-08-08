#!/usr/bin/env python3

import pandas as pd

def suicide_fractions():
    df = pd.read_csv("src/who_suicide_statistics.csv", index_col="country")
    df["mean"] = df["suicides_no"] / df["population"]
    groups = df.groupby("country")
    suicides = groups["mean"].mean()

    return suicides
    
def suicide_weather():
    suicide_data = suicide_fractions()
    weather_data = pd.Series(pd.read_html("src/List_of_countries_by_average_yearly_temperature.html", index_col="Country")[0]["Average yearly temperature (1961–1990, degrees Celsius)"])
    weather_data = weather_data.str.replace("\u2212", "-").astype(float)

    df = pd.merge(weather_data, suicide_data, left_index=True, right_index=True)

    common = len(suicide_data.index.intersection(weather_data.index))
    correlation = df.corr(method='spearman').iloc[0, 1]
    return (len(suicide_data), len(weather_data), common, correlation)

def main():
    a, b, c, d = suicide_weather()

    print(f"Suicide DataFrame has {a} rows")
    print(f"Temperature DataFrame has {b} rows")
    print(f"Common DataFrame has {c} rows")
    print(f"Spearman correlation: {d:.1f}")

if __name__ == "__main__":
    main()
