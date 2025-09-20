'''This is a program where it returns the missing number of n.
for example if the list element is [2,3,4,1] and n = 5 then the missing term in the list is 5.
another example lst=[10,9,8,7,6,5,3,2,1] and here the n would be 10 and the missing number is 4 so the program should return 4 as the answer.
the numbers in the list should be within the value of n.
'''
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
 





