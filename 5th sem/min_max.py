from array import *

a= array('i',[])

def minmax(a,low,high):
    if low == high:
        return a[low],a[high]
    elif high-low == 1:
        if a[low] < a[high]:
            return a[low],a[high]
        else:
            return a[high],a[low]
    else:
        mid = (low+high) // 2
        lmin,rmin = minmax(a,low,mid)
        lmax,rmax = minmax(a,mid+1,high)

        if lmin < rmin:
            min2 = lmin
        else:
            min2 = rmin

        if lmax > rmax:
            max2 = lmax
        else:
            max2 = rmax
        
    return min2,max2

n = int(input("Enter no of array elements:"))

for i in range (n):
    ele = int(input("Enter array elements:"))
    a.append(ele)

min1,max1 = minmax(a,0,n-1)

print("The min element is",min1)
print("The max element is",max1)

