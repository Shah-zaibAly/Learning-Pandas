import pandas as pd

# Data Cleaning - Dropping Irrelevent Columns

df = pd.read_csv("Pokeamon.csv")


df = df.drop(columns=["No","Legendary"])  # reurning a new Dataframe with the columns removed

# If you want to modify the same DataFrame directly:
df.drop(columns=["No","Legenadary"], inplace=True)  # this changes df itself

# If you are not sure a column exists, use errors="ignore":
df = df.drop(columns=["No","Legendary"], errors="ignore")

# If you know the column positions instead of names, you can also drop using df.columns[...]
df = df.drop(df.columns[[0,6]], errors="ignore", axis=1)
print(df)



