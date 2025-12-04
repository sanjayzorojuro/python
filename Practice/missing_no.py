def missing(n):
    lst=[]
    for i in range(n-1):
        ele=int(input("Enter n-1 elements missing: "))
        lst.append(ele)
    add1=n*(n+1)/2
    add2=sum(lst)
    return(add1-add2)
        


n=int(input("Enter the length of the element:"))
print(missing(n))
