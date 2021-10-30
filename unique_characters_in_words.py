str="abc"
reverse=""
index=0+1
while index<=len(str):
    reverse+=str[-index]
    index+=1
print(reverse)