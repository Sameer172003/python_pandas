# Arithmetic Operators in Pandas 

import pandas as pd

var=pd.DataFrame({"A":[1,2,3,4],
                  "B":[5,6,7,8]})
print(var)
print()
var["C"]=var["A"]+var["B"]
print(var)
print()
var["C"]=var["A"]-var["B"]
print(var)
print()
var["C"]=var["A"]*var["B"]
print(var)
print()
var["C"]=var["A"]/var["B"]
print(var)
print()
# Logical Operators

var1=pd.DataFrame({"A":[10,20,30,40],
                  "B":[50,60,70,80]})
var1["D"]=var1["A"] <= 20
var1["E"]=var1["B"] >= 20
print(var1)
print()
