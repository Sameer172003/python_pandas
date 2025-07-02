# Write CSV using Pandas (Create a CSV File)

import pandas as pd

dic={"A":[1,2,3,4],
     "B":[5,6,7,8],
     "C":[9,10,11,12]}
var=pd.DataFrame(dic)
print(var)

# Update index and header in csv

var.to_csv("Test_new.csv")
var.to_csv("Test_new.csv1",index=False,header=[1,2,3])
