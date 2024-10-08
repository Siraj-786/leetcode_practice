class Solution:
    def minSwaps(self, s: str) -> int:
        q=[]
        ans=0
        for i in range(len(s)):
            if s[i]=="[" :
                q.append(s[i])
            else :
                if q :
                    q.pop(-1)
                else :
                    ans+=1 
        return (ans+1)//2



        