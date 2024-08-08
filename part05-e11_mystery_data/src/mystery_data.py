#!/usr/bin/env python3

import pandas as pd
from sklearn.linear_model import LinearRegression

def mystery_data():
    df = pd.read_csv("src/mystery_data.tsv", sep="\t")
    model = LinearRegression(fit_intercept=False)
    model.fit(df.loc[:, ["X1", "X2", "X3", "X4", "X5"]], df.loc[:, "Y"])

    return model.coef_

def main():
    coefficients = mystery_data()
    # print the coefficients here
    for i in range(len(coefficients)):
        print(f"Coefficient of X{i + 1} is {coefficients[i]}")
    
if __name__ == "__main__":
    main()
