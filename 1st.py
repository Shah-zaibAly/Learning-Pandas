import pandas as pd

# A Pandas Series is a one-dimensional labeled array, like a single column in a spreadsheet.
# It can hold numbers, strings, booleans, or even Python objects, and every value has an index label.

# You can create a Series from:
# a list, a NumPy array, a dictionary, a single scalar value with an index.

s = pd.Series([104, 99, 44])
print(s)
print()

roomNumbs = [101, 102, 103, 104, 105]
s1 = pd.Series(roomNumbs, index=["Room1", "Room2", "Room3", "Room4", "Room5"])
print(s1)
print()

s2 = pd.Series({"x":45, "y":78, "z":97})
print(s2)
print()

# Accessing Values
s3 = pd.Series([1,2,3,4,5], index=['a','b','c','d','e'])
# by position
print(s3[0])
print(s3[4])
# by label
print(s3['b'])
print(s3['e'])
