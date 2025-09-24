class Solution():
    def sortedSquares(self, nums):
        sq=[]
        for i in range(len(nums)):
            sq.append(nums[i]*nums[i])
      
        for i in range(len(sq)-1):
            min=i
            for j in range(i+1,len(sq)):
                if sq[j]<sq[min]:
                    min=j
            sq[i],sq[min]=sq[min],sq[i]
        return sq

nums=[-2,-3,4,6,7]
ob1=Solution()
print(ob1.sortedSquares(nums))