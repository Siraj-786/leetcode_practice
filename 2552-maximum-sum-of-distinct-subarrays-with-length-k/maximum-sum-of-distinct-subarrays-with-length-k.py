class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        ans=0
        d=defaultdict(int)
        s=0
        j=0
        for i in range(len(nums)):
            while nums[i] in d :
                d[nums[j]]-=1 
                s-=nums[j]
                if d[nums[j]]==0 :
                    del d[nums[j]]
                j+=1 
            d[nums[i]]+=1
            s+=nums[i] 
            while i-j+1>k:
                d[nums[j]]-=1 
                s-=nums[j]
                if d[nums[j]]==0 :
                    del d[nums[j]]
                j+=1 
            if len(d)==k :
                ans=max(ans,s)
            # print(d)
        return ans

        