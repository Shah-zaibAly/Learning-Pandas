import pandas as pd

# Excercise - Searching a Pokeamon by a name.

df = pd.read_csv('Pokeamon.csv', index_col="Name")
Pokeamon = input("Enter a Pokeamon name: ")

try:
    print(df.loc[Pokeamon])
except KeyError:
    print(f"{Pokeamon} not found.")