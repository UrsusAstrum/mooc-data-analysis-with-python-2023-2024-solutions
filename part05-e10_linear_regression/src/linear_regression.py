#!/usr/bin/env python3

import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def fit_line(x, y):
    model = LinearRegression()
    model.fit(x[:,np.newaxis], y)
    
    return model.coef_[0], model.intercept_
    
def main():
    X = np.linspace(1, 10, 20)
    y = X + 0.1 * np.random.randn(20)
    m, c = fit_line(X, y)
    print(f"Slope: {m}")
    print(f"Intercept: {c}")
    plt.scatter(X, y)
    plt.plot(X, m * X + c)
    plt.show()

if __name__ == "__main__":
    main()
