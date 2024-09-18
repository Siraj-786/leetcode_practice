class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        num=[str(i) for i in nums]
        num.sort(key=lambda x : x*10,reverse=True)
        if num[0]=="0" :
            return "0"
        return "".join(num)