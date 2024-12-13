class Solution:
    def findScore(self, nums: List[int]) -> int:
        visited=set()
        val_index=[(nums[i],i) for i in range(len(nums))]
        val_index.sort()
        ans=0
        for ele in val_index :
            if ele[1] not in visited :
                ans+=ele[0]
                visited.add(ele[1])
                visited.add(ele[1]-1)
                visited.add(ele[1]+1)
        return ans 


        