class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        q=[]
        for i in range(len(s)):
            if s[i]=="(" :
                q.append(i)


        ans=0
        for i in range(len(s)):
            if s[i]==")" :
                if q and q[0]<i :
                    q.pop(0)
                else :
                    ans+=1
        if q :
            ans+=len(q)
        return ans

        