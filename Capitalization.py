s=input()
l=[i for i in s]

for i in range(len(l)):
    if i==0:
        new=l[i].capitalize()
        print(new,end="")
    else:
        print(l[i],end="")
        
        
