from typing import List
class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        lis=[i for i in range(n)]
        s=set(lis)
        for i in edges:
            # delete i[1] from set s
            s.discard(i[1])
        if len(s)==1:
            return list(s)[0]
        return -1