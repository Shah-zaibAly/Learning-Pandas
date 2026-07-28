import pandas as pd

# groupby() is used to split data into groups, apply a function to each group, and combine the results.

# Example 1
data = {
    "Name": ["Ali", "Sara", "Ayan", "Zara", "Hassan"],
    "Class": ["A", "B", "A", "B", "A"],
    "Marks": [85, 90, 78, 92, 88]
}

df = pd.DataFrame(data)

print(df.groupby("Class")["Marks"].mean())
print()
print()
print()

#Example 2
df1 = pd.read_csv("Pokeamon.csv")

print(df1.groupby("Type1")[["Height","Weight"]].mean())