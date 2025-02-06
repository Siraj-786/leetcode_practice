class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        s=defaultdict(int)
        ans=0
        nums.sort()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                k=nums[i]*nums[j] 
                if k in s :
                    ans+=(2*(2*s[k]))
                s[k]+=1 
        return 2*ans 

        