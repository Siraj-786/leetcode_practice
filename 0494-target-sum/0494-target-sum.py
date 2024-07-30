from typing import List
from collections import defaultdict

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        
        d=defaultdict(int)
        d[0]=1 
        
        for ele in nums :
            temp=defaultdict(int)
            for key in d:
                temp[key+ele]+=d[key]
                temp[key-ele]+=d[key]
            d=temp
        return d[target]
