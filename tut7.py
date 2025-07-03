# CSV File Function  using Pandas 

import pandas as pd

csv_1=pd.read_csv("C:\\Users\\ojhas\\Dropbox\\PC\\Downloads\\test_data.csv")

print(csv_1)

print(csv_1.index)

print(csv_1.columns)

print(csv_1.describe())

print(csv_1.head(3))

print(csv_1.tail(3))

print(csv_1[6:13])

print(csv_1.columns.array) 

print(csv_1.to_numpy())

print(csv_1.sort_index(axis=0,ascending=False))

print(csv_1.sort_values(by="Age"))

csv_1.loc[0,"Name"]="Sameer"
print(csv_1)

print(csv_1.loc[[2, 3], ["Name", "Age"]])

print(csv_1.drop("Age",axis=1))
