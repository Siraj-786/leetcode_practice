class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        c1=Counter([i for i in s1.split(" ")])
        ans=set()
        c2=Counter([i for i in s2.split(" ")])
        # print(c1,c2)
        for i in c1 :
            # print(i,c1[i])
            if c1[i]==1 and i not in c2 :
                ans.add(i)
        for i in c2 :
            if c2[i]==1 and i not in c1 :
                ans.add(i)
        # print(ans)
        return list(ans)
        