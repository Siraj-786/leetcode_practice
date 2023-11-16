class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        for i in range(17):
            if bin(i)[2:].rjust(len(nums),"0") not in nums :
                return bin(i)[2:].rjust(len(nums),"0")
        