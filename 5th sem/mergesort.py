from array import *
import random,time

def mergesort(a):
    if len(a) <= 1:
        return a
    mid = len(a) // 2
    left = mergesort(a[ :mid])
    right = mergesort(a[mid: ])
    return merge(left,right)

def merge(left,right):
    res= []
    i=j=0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i+=1
        else:
            res.append(right[j])
            j+=1
        
    res.extend(left[i:])
    res.extend(right[j:])


    return res

a = array('i',[])

for i in range(5005):
    a.append(random.randrange(5000))

start = time.time()
print("Array before sorting is",a)

print("The starting time is :",start)

sortedd = mergesort(a)

print("Array after sorting is:",sortedd)

end = time.time()
print("The end time is :",end)

diff = end-start
print("The total time taken is:",diff)


