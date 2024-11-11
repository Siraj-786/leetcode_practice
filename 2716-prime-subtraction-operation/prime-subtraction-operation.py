class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:

        def sieve(n):
            p=[1]*(n+2)
            for i in range(2,n):
                k=2
                while k*i<=n :
                    p[k*i]=0 
                    k+=1 
            return [i for i in range(n+2) if p[i]==1][2:] 
        s=sieve(1000)
        # print(s)
        # return False

        for i in range(len(nums)-2,-1,-1):
            while nums[i+1]<=nums[i] :
                for k in range(len(s)) :
                    if nums[i+1]>nums[i]-s[k] :
                        nums[i]=nums[i]-s[k] 
                        break 
                break 
        # print(nums)
        if nums[0]<=0 :
            return False 
        return nums==sorted(nums) 

        