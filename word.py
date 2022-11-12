n=input()
l=[i for i in n]
upper=0
lower=0

for i in l:
    if i.isupper():
        upper=upper+1
    else:
        lower=lower+1
        
if upper>lower:
    for i in l:
        print(i.upper(),end="")
elif lower>upper:
    for i in l:
        print(i.lower(),end="")
else:
    for i in l:
        print(i.lower(),end="")
    
