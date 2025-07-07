# PivotTable and Melt in pandas

import pandas as pd

var=pd.DataFrame({"days":[1,2,3,4,5,6],"eng":[12,11,13,10,14,15],"maths":[13,14,11,12,10,15]})

print(pd.melt(var))

print(pd.melt(var,id_vars=["days"]))

print(pd.melt(var,id_vars=["days"],var_name="subjects",value_name="marks"))

# print(var)

var1=pd.DataFrame({"days":[1,2,3,4,5,6],"st_name":["a","b","c","a","b","c"],"eng":[12,11,13,10,14,15],"maths":[13,14,11,12,10,15]})

print(var1.pivot(index="days",columns="st_name"))