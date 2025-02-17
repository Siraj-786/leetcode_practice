class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        s=set()
        for i in range(1,len(tiles)+1):
            for ele in permutations(tiles,i):
                s.add(ele)
        return len(s)
        
                  
        