from typing import List
from collections import defaultdict

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        d=defaultdict(int)
        d[0]=1
        s=sum(nums)
        if s%2:
            return False
        half=s//2
        
        for ele in nums:
            for i in range(half,-1,-1):
                if d[i]:
                    d[i+ele]=1
            if d[half]:
                return True
        return False
