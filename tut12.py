# Group by in pandas

import pandas as pd

var =pd.DataFrame({"name":["a","b","c","d","a","b","a","c","c"],
                   "s_1":[12,22,17,18,15,17,21,20,19],
                   "s_2":[21,22,20,17,16,23,14,19,18]})
# print(var)

var_new=var.groupby("name")

for x,y in var_new:
    print(x)
    print(y)

print()

print(var_new.get_group("a"))

print(var_new.min())

print(var_new.max())

print(var_new.mean())



