import pandas as pd 

# Selection by Row

df = pd.read_csv("Pokeamon.csv", index_col="Name")
# index_col means that we are assigning a column which will serve as index

print(df)  # in this Name will serve as index
print(df.loc["Pikachu"])  # selection by index
print(df.loc["Charizard", ["Height","Weight"]])  # this will only display height and weight for charizard
print(df.loc["Charizard":"Blastoise", ["Type1","Type2"]])  # this will display all the things bw charizard and blastoise including them too
