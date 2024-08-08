#!/usr/bin/env python3

import pandas as pd
from sklearn import linear_model
from sklearn.linear_model import LinearRegression


def coefficient_of_determination():
    df = pd.read_csv("src/mystery_data.tsv", sep="\t")
    model = LinearRegression(fit_intercept=True)
    model.fit(df.loc[:, ["X1", "X2", "X3", "X4", "X5"]], df.loc[:, "Y"])
    scores = [model.score(df.loc[:, ["X1", "X2", "X3", "X4", "X5"]], df.loc[:, "Y"])]
    for i in df.columns:
        x = df.loc[:, i].values.reshape(-1, 1)
        model.fit(x, df.loc[:, "Y"])
        scores.append(model.score(x, df.loc[:, "Y"]))
    return scores
    
def main():
    scores = coefficient_of_determination()
    print(f"R2-score with feature(s) X: {scores[0]}")
    for i in range(1, 6):
        print(f"R2-score with feature(s) X{i}: {scores[i]}")

if __name__ == "__main__":
    main()
