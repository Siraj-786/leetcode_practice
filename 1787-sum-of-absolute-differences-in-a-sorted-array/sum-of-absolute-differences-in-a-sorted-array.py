class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        s=sum(nums)
        ans=[]
        prev_sum=0
        for i in range(len(nums)):
            ans.append(abs(s-nums[i]*(len(nums)-i))+abs(prev_sum-nums[i]*(i)))
            s-=nums[i]
            prev_sum+=nums[i]
        return ans
        