class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dic=set(wordDict)
        dp=[0]*(len(s)+1)

        for i in range(len(s)):
            dp[i+1]=dp[i]+1
            # print(dp)
            for j in range(i,-1,-1):
                k=s[j:i+1]
                # print(i,k)
                if k in dic :
                    dp[i+1]=min(dp[i+1],dp[j])
            # print(dp)
        if dp[-1] :
            return False 
        return True 
        