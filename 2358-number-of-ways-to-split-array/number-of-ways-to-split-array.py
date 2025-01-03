
from typing import List

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        ans = 0
        total = sum(nums)
        prefix_sum = 0
        
        for i in range(len(nums) - 1):
            prefix_sum += nums[i]
            suffix_sum = total - prefix_sum
            
            if prefix_sum >= suffix_sum:
                ans += 1
        
        return ans
