#!/usr/bin/env python3

import pandas as pd
import numpy as np

def read_series():
    vals = []
    index = []

    while True:
        input_data = input()
        if len(input_data) == 0:
            break
        input_data = input_data.split()
        if len(input_data) > 2:
            raise Exception
        
        index.append(input_data[0])
        vals.append(input_data[1])
        
    return pd.Series(vals, index=index)

def main():
    pass

if __name__ == "__main__":
    main()
