import pandas as pd

# 2) DataFrames

x=[4,5,6,7,8]

# Converting List into DataFrames

var=pd.DataFrame(x)
print(var)
print(type(var))

# Converting Dictionary into DataFrames

dic={"name":['python','java','c'],
     "popularity":[12,11,13],
     "rank":[2,1,3]}

ans=pd.DataFrame(dic)
print(ans)

# Getting particular column

ans1=pd.DataFrame(dic,columns=["name"])
print(ans1)

# How to set particular index

ans2=pd.DataFrame(dic,index=['a','b','c'])
print(ans2)


# Getting values from DataFrames

print(ans["name"][1])


# Converting List of List into DataFrames

list_1=[[1,2,3,4],[5,6,7,8]]
res=pd.DataFrame(list_1)
print(res)
print(res[2][1]) 


# Convert Series into DataFrames

sr={"s":pd.Series([1,2,3,4]),
    "r":pd.Series([5,6,7,8])
    }

res1=pd.DataFrame(sr)
print(res1)
