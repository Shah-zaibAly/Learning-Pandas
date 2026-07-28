import pandas as pd

# Selection by Column

df = pd.read_csv("Pokeamon.csv")   

print(df["Name"])
print(df["Height"])
print(df[["Name", "Type1", "Legendary"]])

