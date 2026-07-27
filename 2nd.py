import pandas as pd

# A Pandas DataFrame is a two-dimensional table-like data structure with rows and columns.
# It is the main object in Pandas for working with structured data, and different columns can store different data types.

# You can create a DataFrame from:
# a dictionary of lists, a list of dictionaries, a NumPy array, a CSV file later using pd.read_csv().

data = {
    "Name": ["ali", "esdeekid", "zara"],
    "Age": [22, 24, 21],
    "Grade": ['A','B+','A']
}

df = pd.DataFrame(data, index=["Student# 01", "Student# 02", "Student# 03"])
print(df)
print()

# add a new column
df["Job"] = ["Software Enginner", "Singer", "Business Consultant"]
print(df)
print()

# add a new row
newRow = pd.DataFrame([{"Name": "saif", "Age": 22, "Grade":'C', "Job": "Unemployed"}], index=["Student# 04"])
df = pd.concat([df, newRow])
print(df)
print()

# Accessing 
print(df["Name"])  # for a column
print(df["Job"])
print(df.loc["Student# 01"])  # for a label-based selection
print(df.iloc[3])  # for a position-based selection

