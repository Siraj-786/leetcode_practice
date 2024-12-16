class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:

        keys_ind=[]
        for i in range(len(nums)):
            keys_ind.append((nums[i],i))
        heapq.heapify(keys_ind)
        while k :
            k-=1 
            p=heapq.heappop(keys_ind)
            a=p[0]*multiplier 
            heapq.heappush(keys_ind,(a,p[1]))
        ans=[0]*len(nums)
        for ele in keys_ind :
            ans[ele[1]]=ele[0]
        return ans 
        