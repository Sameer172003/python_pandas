# Handling Missing Data (Replace and Interpolate)

import pandas as pd

csv_1=pd.read_csv("C:\\Users\\ojhas\\Dropbox\\PC\\Downloads\\test2_data.csv")


print(csv_1.replace(to_replace=54,value=34))

print(csv_1.replace(to_replace="Tony Davis",value="Sameer"))

print(csv_1.replace("[A-Za-z]","c",regex=True))

print(csv_1.replace({"Name":'[A-Z]'},"sameer",regex=True))

print(csv_1.replace(54,method="ffill"))   # forward filling

print(csv_1.replace(54,method="bfill"))   # backward filling

csv_1=pd.read_csv("C:\\Users\\ojhas\\Dropbox\\PC\\Downloads\\test3_data.csv")
# print(csv_1)

print(csv_1.interpolate(method="linear"))



