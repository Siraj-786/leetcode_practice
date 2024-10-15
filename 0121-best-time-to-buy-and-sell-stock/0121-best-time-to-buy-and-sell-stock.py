class Solution:
    def maxProfit(self, prices: List[int]) -> int:


        suff_max=[prices[-1]]
        for i in range(len(prices)-2,-1,-1):
            suff_max.append(max(suff_max[-1],prices[i]))
        suff_max=suff_max[::-1]
        ans=0 
        for i in range(len(prices)):
            ans=max(ans,suff_max[i]-prices[i])
        return ans 
        