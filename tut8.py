# Handling Missing Data (Dropena & Fillna)

import pandas as pd

csv_1=pd.read_csv("C:\\Users\\ojhas\\Dropbox\\PC\\Downloads\\test_data.csv")

print(csv_1.dropna()) # deleting rows

print(csv_1.dropna(axis=1))  # deleting columns

print(csv_1.dropna(how="any")) # If you want to delete the column and row where NaN is present then use "any"
print(csv_1.dropna(how="all")) # If you want to delete the row where all columns have NaN values then use "all"

print(csv_1.dropna(subset=["Age"]))

print(csv_1.dropna(inplace=True))

print(csv_1.dropna(thresh=1)) # We can use 2,3,4,.... accordingly to delete the NaN values


csv_1=csv_1.fillna({"Age":35,"Salary":75000.05})

print(csv_1)

csv_1=csv_1.fillna(method="ffill")  # forward filling
csv_1=csv_1.fillna(method="bfill")  # backward filling

csv_1=csv_1.fillna(method="ffill",axis=1)

print(csv_1)
