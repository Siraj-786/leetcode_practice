class Solution:
    def minCut(self, s: str) -> int:

        dp=[i for i in range(len(s))]


        for i in range(1,len(s)):
            j=i
            while j>=0 :
                # print(j,i)
                if j==0 :
                    if s[j:i+1]==s[j:i+1][::-1] :
                        dp[i]=0
                else :
                    if s[j:i+1]==s[j:i+1][::-1] :
                        if j==0 :

                            dp[i]=min(dp[i],0)
                        else :
                            dp[i]=min(dp[i],1+dp[j-1])
                j-=1 
            # print(dp)
        return dp[-1]





        