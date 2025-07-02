# Insert Data in Pandas 

import pandas as pd
var=pd.DataFrame({"A":[1,2,3,4],
                  "B":[5,6,7,8]})

var.insert(2,"C",var["A"])
var.insert(3,"D",[9,10,11,12])
var["E"]=var["B"][:3]
print(var)
print()


# Delete Data in Pandas 

ans=var.pop("C")
print()
print(ans)

print()
del var["D"]
print(var)
