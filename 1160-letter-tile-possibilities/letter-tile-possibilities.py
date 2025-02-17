class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        ss=set()
        def permutations(s,i,curr,pos,need):
            if len(curr)==need :
                ss.add(curr)
                return
            else :
                for i in range(len(s)):
                    if i not in pos :
                        curr+=s[i]
                        permutations(s,i,curr,pos+[i],need)
                        curr=curr[0:-1]
        # permutations("abc",0,"",[],2)
        print(ss)

        for i in range(1,len(tiles)+1):
            permutations(tiles,0,"",[],i)
        return len(ss)
        
                  
        