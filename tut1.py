import pandas as pd
x=[3,4,5,6,7,8]

# 1) Series

# Converting List into Series
var=pd.Series(x)
print(var)
print(type(var))

# Getting values from series

print(var[2])

# How to set particular index 

y=[4,5,6]
res=pd.Series(y,index=['a','b','c'])

 
# We can also change the data type

res=pd.Series(y,index=['a','b','c'],dtype="float")
print(res)

# Converting Dictionary into Series

dic={"name":['python','java','c'],
     "popularity":[12,11,13],
     "rank":[2,1,3]}

var1=pd.Series(dic)

print(var1) 


# Why we use pandas over numpy

a1=[1,2,3,4]
ans1=pd.Series(a1)
a2=[5,6,7]
ans2=pd.Series(a2)

print(ans1+ans2)

# --> It perform operations even data is missing




