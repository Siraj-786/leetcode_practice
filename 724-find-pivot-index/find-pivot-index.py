class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l=0
        r=sum(nums)
        for i in range(len(nums)):
            if i==0 :
                l=0 
            else :
                l+=nums[i-1]
            k=r-(l+nums[i])
            if l==k :
                return i
        return -1 


        