import pandas as pd

# Importing and Reading

df = pd.read_csv("Pokeamon.csv")
print(df)   # prints first 5 and list 5 rows
print(df.to_string())