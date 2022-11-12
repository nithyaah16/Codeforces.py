n=int(input())
s=str(n)
count=0

for i in s:
    if int(i)==4 or int(i)==7:
        count=count+1
state=True
c=str(count)
for i in c:
    if i=="4" or i=="7":
        continue
    else:
        state=False
        break
if state==True:
    print("YES")
else:
    print("NO")
    
