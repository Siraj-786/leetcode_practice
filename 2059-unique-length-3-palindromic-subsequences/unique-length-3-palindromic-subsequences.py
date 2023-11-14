class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        char_set=set(s)



        def index_last(s,i):
            for ind in range(len(s)-1,-1,-1):
                print(s[ind],ind)
                if s[ind]==i :
                    return ind

        

        ans=0
        for i in char_set :
            l=s.index(i)
            r=index_last(s,i)  
            if r>(l+1) :         #       a.....a   finding all the distinct characters between them including a as well
                char=set()
                for ch in range(l+1,r):
                    char.add(s[ch])
                ans+=len(char)

        return ans

        