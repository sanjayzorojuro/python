def findsub(s,d):
    def rec(index,csum,cset):
        if csum == d:
            subset.append(list(cset))
            return
        if csum > d or index == len(ele):
            return
        rec(index+1,csum+ele[index],cset+[ele[index]]) 
        rec(index+1,csum,cset)
    subset=[]
    ele = list(s)
    rec(0,0,[])
    return subset

s = set(map(int,input("Enter comma seperate values:").split(',')))
d = int(input("Enter weight:"))

res = findsub(s,d)

if res:
    print("The subset for:",d)
    for sub in res:
        print(sub)
else:
    print("There are no subset for ",d)