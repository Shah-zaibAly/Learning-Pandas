import pandas as pd

# Data Cleaning - Fix Inconsistent Values

df = pd.read_csv("Pokeamon.csv")

# Examples you’ll see a lot:
# "Fire", "fire ", "FIRE"
# "Male", "M", "male"
# "N/A", "NA", "NaN", ""
# Goal: turn all of these into one standard value so grouping, filtering, and analysis work correctly.

# In Pandas, you mainly use string cleaning methods and replace() for this.

# 1) Basic string cleaning
# First clean whitespace and casing so values become comparable:
df["Type1"] = df["Type1"].str.strip().str.lower()   # eg: " Grass " -> "grass"

# 2) Replacing specific wrong values with replace()

# Replacing only one value
df["Type1"] = df["Type1"].replace("grass","vegeterian")  # replaces grass with vegeterian

# Replacing more than one value
df["Gender"] = df["Gender"].replace(
    ["M", "male", "MALE", "m"], "Male"
)

# using a mapping Dictionary 
mapping = {
    "firee": "fire",
    "fir": "fire",
    "water-type": "water"
}

df["Type1"] = df["Type1"].replace(mapping)
