n=int(input())
for i in range(n+1,19000):
    l=[]
    s=str(i)
    for j in s:
        if j not in l:
            l.append(j)
    if len(l)==4:
        res=i
        break

print(res)
    
