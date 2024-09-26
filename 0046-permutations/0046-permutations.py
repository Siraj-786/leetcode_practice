class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]

        def rec(arr,visited):
            if len(arr)==len(nums):
                ans.append(arr)
                return 

            for i in range(len(nums)):
                if not visited[i] :
                    visited[i]=1 
                    rec(arr+[nums[i]],visited)
                    visited[i]=0
        rec([],[0]*len(nums))
        return ans

        