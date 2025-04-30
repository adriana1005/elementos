import pandas as pd

df = pd.read_csv("ganhomensal.csv", encoding = "latin1")
missing_values = df.isnull().sum()

print(missing_values)