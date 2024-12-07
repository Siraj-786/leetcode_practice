class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:

        def pieces(arr,v):
            c=0
            for i in range(len(arr)):
                c+=math.ceil(arr[i]/v)
            return c-len(arr) 

        l,r=1,10**9 
        while l<r :
            m=(l+r)//2
            if pieces(nums,m) <=maxOperations :
                r=m
            else :
                l=m+1 
        for i in range(l,r+1):
            if pieces(nums,i) :
                return i
        return max(nums)
         
        