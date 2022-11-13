ip=input().split()
n=int(ip[0])
m=int(ip[1])

def prime(n):
    flag=False
    for i in range(2,n):
        if n%i==0:
            flag=True
    return flag

for j in range(n+1,m+1):
    f=prime(j)
    if j!=m:
        if f==False:
            print("NO")
            break
    else:
        if prime(j)==False:
            print("YES")
        else:
            print("NO")
    
    
    
