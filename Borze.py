n1=input()
n=[]
for i in n1:
    n.append(i)
    
l=len(n)
lst=[]
lst1=[]

for i in range(l):
    if len(lst1)-1==i:
        continue
    elif n[i]=='.':
        lst.append(0)
        lst1.append(n[i])
    elif n[i]=='-' and n[i+1]=='-':
        lst.append(2)
        lst1.append(n[i])
        lst1.append(n[i+1])
       
    elif n[i]=='-' and n[i+1]=='.':
        lst.append(1)
        lst1.append(n[i])
        lst1.append(n[i+1])
        
        
for i in lst:
    print(i,end='')
