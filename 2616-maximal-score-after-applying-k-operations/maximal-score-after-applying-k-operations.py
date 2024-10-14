class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans=0 
        for i in range(k):
            p=nums.pop(-1)
            ans+=p 
            insort(nums,math.ceil(p/3))
        return ans 
        