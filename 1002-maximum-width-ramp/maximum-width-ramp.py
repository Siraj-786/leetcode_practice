class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:


        dec=[nums[0]]
        ind=[0]
        ans=0
        for i in range(1,len(nums)):
            if nums[i]<dec[-1] :
                ind.append(i)
                dec.append(nums[i])
        for j in range(len(nums)-1,-1,-1) :
            while dec and dec[-1]<=nums[j] :
                ans=max(ans,j-ind[-1])
                ind.pop(-1)
                dec.pop(-1)
        return ans 



        
            
        