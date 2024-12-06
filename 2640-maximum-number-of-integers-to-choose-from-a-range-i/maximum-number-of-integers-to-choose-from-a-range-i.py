class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        unbanned=[]
        s=set(banned)
        for i in range(1,n+1):
            if i not in s :
                unbanned.append(i)
        if not unbanned :
            return 0
        pre=[unbanned[0]]
        # print(pre)
        for i in range(1,len(unbanned)):
            pre.append(pre[-1]+unbanned[i])
        # print(pre)
        return bisect.bisect_right(pre,maxSum)
        