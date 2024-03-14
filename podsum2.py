
import numpy as np
import pandas as pd

df = pd.read_csv('exchen2.csv')
#print(df.groupby(['exchange ask', 'exchange bid'])['profit'].sum())
df = df.groupby(['exchange ask', 'exchange bid'])['profit'].sum()
df = pd.DataFrame(df)
print(df.sort_values('profit').to_string())

