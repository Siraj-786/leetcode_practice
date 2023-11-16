class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        s=set(nums)
        for i in range(17):
            if bin(i)[2:].rjust(len(nums),"0") not in s :
                return bin(i)[2:].rjust(len(nums),"0")
        