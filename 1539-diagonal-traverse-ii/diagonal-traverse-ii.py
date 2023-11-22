from typing import List
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        l1=[]
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                l1.append((i+j,i,j,nums[i][j]))
        sorted_data = sorted(l1, key=lambda x:(x[0],-x[1]))
        ans=[]
        for i in sorted_data:
            ans.append(i[3])
        return ans