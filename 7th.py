import pandas as pd

# Filtering 

df = pd.read_csv("Pokeamon.csv")

tallPokeamon = df[df["Height"] > 2]
HeavyPokeamon = df[df["Weight"] > 100]
Legendary = df[df["Legendary"] == 1]
waterPokeamon = df[(df["Type1"] == "Water") | (df["Type2"] == "Water")]

print(waterPokeamon)