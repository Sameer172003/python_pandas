# Read CSV using Pandas

import pandas as pd

csv_1=pd.read_csv("C:\\Users\\ojhas\\Dropbox\\PC\\Downloads\\random_data.csv")

# print(csv_1)

# Get particular row data

csv_2=pd.read_csv("C:\\Users\\ojhas\\Dropbox\\PC\\Downloads\\random_data.csv",nrows=1)

# print(csv_2)

# Get column data

# csv_3=pd.read_csv("C:\\Users\\ojhas\\Dropbox\\PC\\Downloads\\random_data.csv",usecols=["Name"])

csv_3=pd.read_csv("C:\\Users\\ojhas\\Dropbox\\PC\\Downloads\\random_data.csv",usecols=[0,2])

# print(csv_3)

# To skip particular rows

csv_4=pd.read_csv("C:\\Users\\ojhas\\Dropbox\\PC\\Downloads\\random_data.csv",skiprows=[1])
print(csv_4)


