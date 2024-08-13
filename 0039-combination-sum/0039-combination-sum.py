


from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        def rec(arr,i,s):
            print(arr)
            if s==target:
                ans.append(arr)
                return

            if i>=len(candidates):
                return
            if s+candidates[i]<=target:
                # rec(arr+[candidates[i]],i+1,s+candidates[i])
                rec(arr+[candidates[i]],i,s+candidates[i])
            rec(arr,i+1,s)
        rec([],0,0)
        return ans