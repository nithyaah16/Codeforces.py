ip=[int(x) for x in input().split()]
n=ip[0]
t=ip[1]

q=input()
q1=[]
for i in q:
    q1.append(i)

for i in range(t):
    ind=[]
    for i in range(0,n-1):
        if q1[i]=="B":
            ind.append(i)

    for i in ind:
        temp=q1[i+1]
        q1[i+1]=q1[i]
        q1[i]=temp
    
res=""
for i in q1:
    res=res+i
print(res)
