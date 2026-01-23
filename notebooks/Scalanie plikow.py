import pandas as pd
import os

output = r"C:\Users\Dell\Desktop\test.csv"
base_dir = r"C:\Users\Dell\Desktop\Pobrane_do_projektu"

first = True

for year in range(2001, 2024):
    for month in range(1, 13):
        plik = f"k_d_{month:02d}_{year}.csv"
        folder = os.path.join(base_dir, plik)

        if os.path.exists(folder):
            df = pd.read_csv(folder, encoding='cp1250')

            df.to_csv(
                output,
                mode="w" if first else "a",
                index=False,
                header=first,
                encoding='utf-8'
            )
            first = False

