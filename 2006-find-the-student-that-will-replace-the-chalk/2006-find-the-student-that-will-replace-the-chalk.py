class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        s=sum(chalk)
        k-=(k//s)*s
        for i in range(len(chalk)):
            if chalk[i]>k :
                return i 
            k-=chalk[i]
        return 0

        