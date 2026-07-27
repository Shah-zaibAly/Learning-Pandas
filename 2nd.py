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



