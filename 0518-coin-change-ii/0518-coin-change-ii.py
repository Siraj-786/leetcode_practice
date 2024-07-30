class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # Initialize the dp array
        dp = [[0 for _ in range(amount + 1)] for _ in range(len(coins) + 1)]
        
        # Base case: There is one way to make amount 0 (by choosing no coins)
        for i in range(len(coins) + 1):
            dp[i][0] = 1
        
        for i in range(1, len(coins) + 1):
            for j in range(1, amount + 1):
                if j >= coins[i - 1]:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]
        
        # Debug prints to understand the internal state
        for ele in dp:
            print(ele)
        
        return dp[-1][-1]
