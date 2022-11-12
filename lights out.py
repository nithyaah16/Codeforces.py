from numpy import *

a=[int(x) for x in input().split()]
b=[int(x) for x in input().split()]
c=[int(x) for x in input().split()]
arr1=array([a,b,c])
arr2=array([[1,1,1],[1,1,1],[1,1,1]])

def change(a,b):
    if a%2!=0:
        if b==0:
            return 1
        else:
            return 0
    else:
        if b==0:
            return 0
        else:
            return 1
        
def change2(a):
    if a==0:
        return 1
    else:
        return 0
    
for r1 in range(3):
    for c1 in range(3):
        arr2[r1][c1]=change(arr1[r1][c1], arr2[r1][c1])
 
        if arr1[r1][c1]%2!=0:
            if r1<2:
                arr2[r1+1][c1]=change2(arr2[r1+1][c1])
          
            if c1<2:
                arr2[r1][c1+1]=change2(arr2[r1][c1+1])
           
            if r1>0:
                arr2[r1-1][c1]=change2(arr2[r1-1][c1])
               
            if c1>0:
                arr2[r1][c1-1]=change2(arr2[r1][c1-1])
              
for i in arr2:
    for j in i:
        print(j,end="")
    print("")
