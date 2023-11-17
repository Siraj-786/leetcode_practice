class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        maxi=0
        nums.sort()
        for i in range(len(nums)//2):
            maxi=max(maxi,nums[i]+nums[(-1)*(i+1)])
        return maxi