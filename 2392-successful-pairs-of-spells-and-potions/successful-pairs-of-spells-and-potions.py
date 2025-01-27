class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        ans=[]
        potions.sort()
        for ele in spells :
            mini=math.ceil(success/ele)
            ind=bisect.bisect_left(potions,mini)
            if ind==len(potions):
                ans.append(0)
                continue
            ans.append(len(potions)-ind)
        return ans  


        