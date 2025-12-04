from array import *
import random
import time

def quicksort(a):
    if len(a) <= 1:
        return a
    pivot = a[0]
              
    left = [x for x in a[1:] if x < pivot]
    right = [x for x in a[1:] if x >= pivot]

    return quicksort(left) + [pivot] + quicksort(right)


a=array("i",[])

for i in range(5005):
    n=random.randrange(5000)
    a.append(n)

size=len(a)

print("The array before sorting :",a)
start=time.time()
print("Thw starting time is:",start)

b = quicksort(a)

print("The array after sorting :",b)    
end=time.time()
print("The ending time is:",end)

diff=end-start
print("The total time taken is :",diff)