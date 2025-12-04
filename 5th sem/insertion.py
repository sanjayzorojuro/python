from array import  *

def ins(a,n):
    for i in range(n):
        v = a[i]
        j = i-1
        while j >= 0 and a[j] > v:
            a[j+1] = a[j]
            j = j-1
        a[j+1] = v
    return a

a = array('i',[])

n = int(input("Enter no of elements:"))

for i in range(n):
    ele = int(input("Enter array elements:"))
    a.append(ele)

print("Array before sorting:",a)
print("Array after sorting:",ins(a,n))

