from collections import defaultdict
from typing import List

class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        total_sum = sum(nums)
        
        # If total sum is less than 2*k, no valid partition can be made
        if total_sum < 2 * k:
            return 0
        
        n = len(nums)
        dp = defaultdict(int)
        dp[0] = 1
        
        # Count subsets with sum less than k
        for num in nums:
            new_dp = dp.copy()
            for s in dp:
                new_sum = s + num
                if new_sum < k:
                    new_dp[new_sum] = (new_dp[new_sum] + dp[s]) % MOD
            dp = new_dp
        
        # Calculate total number of ways to partition into two groups
        total_partitions = pow(2, n, MOD)
        
        # Subtract subsets that don't satisfy the condition
        invalid_partitions = 0
        for s in dp.values():
            invalid_partitions = (invalid_partitions + s) % MOD
        
        # We subtract twice since invalid partitions could be in either group
        result = (total_partitions - 2 * invalid_partitions) % MOD
        
        return result
