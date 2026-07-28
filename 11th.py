import pandas as pd

# Data Cleaning - Missing Data Handling
# missing data handling in Pandas mainly means detecting, dropping, or filling NaN values.
# The main tools are isnull() / isna(), dropna(), and fillna()

df = pd.read_csv("Pokeamon.csv")

# 1) Detect missing values
print(df.isna())  # isna() gives True/False for each cell
print(df.isna().sum())  # sum() shows how many missing values each column has.

# 2) Drop missing values
df = df.dropna()  # By default, this removes rows that have at least one missing value.
df = df.dropna(how=all)  # Drops only rows where all values are missing.
df = df.dropna(subset=["Height","Type2"])  # Drops rows only if missing values appear in those columns.
df = df.dropna(axis=1)  # Drops columns that contain missing values.

# 3) Fill missing values
df["Type2"] = df["Type2"].fillna("Unknown")  # replaces the missing values with "Unknown"
df["Weight"] = df["Weight"].fillna(df["Weight"].mean())  # This fills missing ages with the average age.
df = df.fillna(method="ffill")  # Forward Fill : uses the previous value to fill the gap.
df = df.fillna(method="bfill")  # Backward Fill : uses the next value to fill the gap.


