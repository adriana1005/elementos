import pandas as pd

df = pd.read_csv(".csv", encoding = "latin1")
missing_values = df.isnull().sum()

print(missing_values)