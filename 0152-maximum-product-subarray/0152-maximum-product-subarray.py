class Solution:
    def maxProduct(self, nums: List[int]) -> int:


        maxi=max(nums)
        pre=1
        for i in range(len(nums)):
            pre*=nums[i]
            maxi=max(maxi,pre)
            if pre==0 :
                pre=1 
        suf=1 
        for i in range(len(nums)-1,-1,-1):
            suf*=nums[i]
            maxi=max(suf,maxi)
            if suf==0 :
                suf=1
        return maxi
            

        