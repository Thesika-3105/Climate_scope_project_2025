import pandas as pd
import numpy as np
import os
file_path = "data/global-weather-repository.csv"
df = pd.read_csv(file_path)
print("Data loaded successfully!")
print("Shape:", df.shape)
print(df.head())
print("\nColumn info:")
print(df.info())
critical_cols = [c for c in df.columns if any(k in c.lower() for k in ["temp", "humid", "precip", "wind"])]
df = df.dropna(subset=critical_cols, how="any")
df = df.fillna(df.mean(numeric_only=True))
if "temperature" in df.columns:
    if df["temperature"].mean() > 100:  # likely Kelvin
        df["temperature"] = df["temperature"] - 273.15
if "temperature" in df.columns:
    df["temperature_norm"] = (df["temperature"] - df["temperature"].min()) / (
        df["temperature"].max() - df["temperature"].min()
    )
if "date" in df.columns:
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df["year_month"] = df["date"].dt.to_period("M")
    monthly = df.groupby(["year_month", "country"], as_index=False).mean(numeric_only=True)
else:
    monthly = df.copy()
os.makedirs("processed", exist_ok=True)
out_path = "processed/cleaned_weather.csv"
monthly.to_csv(out_path, index=False)
print(f"Cleaned dataset saved → {out_path}")
summary = {
    "num_rows": len(monthly),
    "columns": monthly.columns.tolist(),
    "missing_values": monthly.isna().sum().to_dict()
}

print("\n=== Summary ===")
for k, v in summary.items():
    print(f"{k}: {v}")

