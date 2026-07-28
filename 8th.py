import pandas as pd

# Aggregate Functions

df = pd.read_csv("Pokeamon.csv")

# Whole Dataframe
# numeric_only is used when in a group of data we also have values other than integers, so it will just use integers
print(df.mean(numeric_only=True))
print(df.sum(numeric_only=True))
print(df.max(numeric_only=True))
print(df.min(numeric_only=True))
print(df.count())

# Single Column 
print(df["Height"].mean())
print(df["Height"].sum())
print(df["Height"].max())
print(df["Height"].min())
print(df["Height"].count())

