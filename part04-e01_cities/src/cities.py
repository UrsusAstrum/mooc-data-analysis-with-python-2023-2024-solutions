#!/usr/bin/env python3

import pandas as pd

def cities():
    index = ["Helsinki", "Espoo", "Tampere", "Vantaa", "Oulu"]
    population = [643272, 279044, 231853, 223027, 201810]
    total_area = [715.48, 528.03, 689.59, 240.35, 3817.52]
    return pd.DataFrame({"Population": population, "Total area": total_area}, index=index)
    
def main():
    return
    
if __name__ == "__main__":
    main()
