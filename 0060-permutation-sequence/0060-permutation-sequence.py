class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        p=list(permutations([i+1 for i in range(n)]))
        # print(p)
        return "".join(str(i) for i in p[k-1])
        