class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        ans=0
        piles.sort()
        for i in range(0,len(piles)//3):
            print(piles[(-2)*(i+1)])
            ans+=piles[(-2)*(i+1)]
        return ans
        