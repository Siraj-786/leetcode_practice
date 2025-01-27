class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=2 :
            return max(nums)
        ans=max(nums)
        maxi=nums[0]
        for i in range(2,len(nums)):
            nums[i]+=maxi 
            ans=max(ans,nums[i])
            maxi=max(maxi,nums[i-1])
        return ans 
        