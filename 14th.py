import pandas as pd

# Data Cleaning - Fixing Data Types and Removing Duplicates

df = pd.read_csv("Pokeamon.csv")

# Fixing Data Types
df["Legendary"] = df["Legendary"].astype(bool)

# Removing Duplicate Values
df = df.drop_duplicates()