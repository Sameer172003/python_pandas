# Join and Append(Concat)

import pandas as pd

var1=pd.DataFrame({"A":[1,2,3,4],"B":[5,6,7,8]})
var2=pd.DataFrame({"C":[10,20],"D":[11,22]})

# print(var1.join(var2))

# print()

# print(var2.join(var1))

# print()

# print(var2.join(var1,how="left"))
# print(var2.join(var1,how="inner"))
# print(var2.join(var1,how="right"))
# print(var2.join(var1,how="outer"))

v1=pd.DataFrame({"A":[1,2,3,4],"B":[5,6,7,8]})
v2=pd.DataFrame({"C":[10,20],"B":[11,22]})

v=pd.concat([v1,v2])
print(v)




