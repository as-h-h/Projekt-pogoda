import os
import time

os.mkdir("C:/Users/Dell/Desktop/Pobrane_do_projektu")

for year in range(2001, 2024):
    for month in range(1, 13):
        output_dir = f"C:\\Users\\Dell\\Desktop\\Pobrane_do_projektu"

        url = f"https://danepubliczne.imgw.pl/data/dane_pomiarowo_obserwacyjne/dane_meteorologiczne/dobowe/klimat/{year}/{year}_{month:02d}_k.zip"

        print("Pobiera url",url)

        os.system(f'powershell Invoke-WebRequest -Uri {url} -OutFile "{year}_{month}.zip"')
        os.system(f'powershell Expand-Archive -Path "{year}_{month}.zip" -Force -DestinationPath {output_dir}')
        for file in os.listdir(f"C:\\Users\\Dell\\Desktop\\Pobrane_do_projektu"):
            if file.startswith('k_d_t'):
                os.remove(f"C:\\Users\\Dell\\Desktop\\Pobrane_do_projektu\\k_d_t_{month:02d}_{year}.csv")

        time.sleep(1)