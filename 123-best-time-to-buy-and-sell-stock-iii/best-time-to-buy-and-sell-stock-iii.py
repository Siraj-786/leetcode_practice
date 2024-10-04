class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prices.append(0)
        prices.append(0)
        pre_min_a=[prices[0]]
        for i in range(1,len(prices)):
            pre_min_a.append(min(pre_min_a[-1],prices[i]))
        print(pre_min_a)
        diffs=[]
        for i in range(len(prices)):
            diffs.append(prices[i]-pre_min_a[i])
        new_diffs=[]
        for i in range(len(diffs)):
            if new_diffs :
                new_diffs.append(max(new_diffs[-1],diffs[i]))
            else :
                new_diffs.append(diffs[i])
        diffs=new_diffs
        suff_max=[prices[-1]]
        for i in range(len(prices)-2,-1,-1):
            suff_max.insert(0,max(suff_max[0],prices[i]))
        max_ans=0
        for i in range(1,len(prices)):
            max_ans=max(max_ans,diffs[i-1]+suff_max[i]-prices[i])
        return max_ans


        