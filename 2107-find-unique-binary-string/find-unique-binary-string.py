class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        s=set(nums)
        l=len(nums)
        for i in range(17):
            p=bin(i)[2:].rjust(l,"0")
            if p not in nums :
                return p
        