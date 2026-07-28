import pandas as pd

# Excercise 

df = pd.read_csv("Prices.csv")

print(df.isna().sum())
print()
print()

mapping = {
    "sports":"athletics",
    "electronics":"gadgets",
    "health":"wellness",
    "books":"volumes",
    "art":"artistry"
}

df["Category"] = df["Category"].str.strip().str.lower().replace(mapping)

df["Price"] = pd.to_numeric(
    df["Price"]
        .str.replace("$","",regex=False)
        .str.replace(",","",regex=False)
        .str.strip,
    errors="coerce"
)

print(df.to_string())

