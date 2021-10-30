array=["go","bat","me","eat","goal","boy","run"]
str1="".join(array)
dict={}
for x in str1:
    if x in dict.keys(): dict[x]+=1
    else: dict[x]=1
for x,y in dict.items():
    if y==1: print(x)
