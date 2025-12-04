# selection sort

from array import *

a = array("i",[])

n=int(input("Enter no of array elements:"))


for i in range(n):
    ele= int(input("Enter array elements:"))
    a.append(ele)

print("Array before sorting is :",a)

for i in range(n-1):
    min = i 
    for j in range(i+1,n):
        if a[j] < a[min]:
            min = j
    a[i],a[min] =  a[min],a[i]

    
print("Array after sorting is :",a)