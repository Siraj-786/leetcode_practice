class Solution:
    def minSteps(self, n: int) -> int:
        dp=[float('inf')]*n
        dp[0]=0
        for i in range(1,n):
            for j in range((i+1)//2):
                l=j+1
                diff=i-j
                if diff%l==0 :
                    dp[i]=min(dp[i],dp[j]+1+diff//l)
        print(dp)
        return dp[-1]        