from pathlib import Path
import csv 
path = Path("sitka_weather_07-2021_simple.csv")
lines = path.read_text(encoding="utf-8").splitlines()
print(lines)