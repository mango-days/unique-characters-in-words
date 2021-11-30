array = [ "go", "bat", "me", "eat", "goal", "boy", "run" ]
array2 = "" .join ( array )
check = []
not_unique = []

for x in array2 :
    if x not in check : check.append ( x )
    else :  not_unique.append ( x )
    
for x in check :
    if x not in not_unique : print ( x )
