# Merging and Concat 

import pandas as pd

# var1=pd.DataFrame({"A":[1,2,3,4],"B":[5,6,7,8]})

# var2=pd.DataFrame({"A":[1,2,3,4],"C":[13,14,15,16]})


var1=pd.DataFrame({"A":[1,2,3,4],"B":[5,6,7,8]})

var2=pd.DataFrame({"A":[1,2,3,5],"C":[13,14,15,16]})

# print(pd.merge(var1,var2,how="inner")) 
# print(pd.merge(var1,var2,how="left")) 
# print(pd.merge(var1,var2,how="right")) 
# print(pd.merge(var1,var2,how="outer")) 

# print(pd.merge(var1,var2,left_index=True,right_index=True))

s1=pd.Series([1,2,3,4])
s2=pd.Series([5,6,7,8])

print(pd.concat([s1,s2]))

print(pd.concat([var1,var2]))



