class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        d=defaultdict(int)
        j=0
        ans=0
        for i in range(len(nums)):
            d[nums[i]]+=1 
            while d[0]>k :
                d[nums[j]]-=1 
                j+=1 
            ans=max(ans,d[0]+d[1])
        return ans 
            

        