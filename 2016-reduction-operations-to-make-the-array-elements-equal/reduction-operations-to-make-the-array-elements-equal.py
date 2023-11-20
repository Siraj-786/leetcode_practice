from collections import defaultdict
from typing import List
class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        d = defaultdict(int)
        for i in nums:
            d[i] += 1
        keys = [i for i in d.keys()]
        val=[d[i] for i in keys]
        z=[y for x,y in sorted(zip(keys,val))]
        ans=0
        for i in range(1,len(z)):
            ans+=i*z[i]
        return ans