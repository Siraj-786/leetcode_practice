class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        s=sum(nums)
        ans=[]
        prev_sum=0
        l=len(nums)
        for i in range(len(nums)):
            ans.append(abs(s-nums[i]*l)+abs(prev_sum-nums[i]*(len(nums)-l)))
            l-=1
            s-=nums[i]
            prev_sum+=nums[i]
        return ans
        