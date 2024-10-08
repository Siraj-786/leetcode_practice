class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[float('inf') for i in range(amount+1)]
        dp[0]=0
        for i in range(len(coins)):
            c=coins[i]
            for a in range(1,amount+1):
                if a>=c :
                    dp[a]=min(dp[a],dp[a-c]+1)
        # print(dp)
        if dp[-1]==float('inf'):
            return -1
        return dp[-1]


        