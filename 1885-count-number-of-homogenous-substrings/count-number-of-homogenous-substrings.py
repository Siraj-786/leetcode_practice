class Solution:
    def countHomogenous(self, s: str) -> int:
        l1=[]
        k=1
        mod=1e9+7
        for i in range(1,len(s)):
            if s[i]!=s[i-1] :
                l1.append(k)
                k=1 
            else :
                k+=1 
        if k :
            l1.append(k)
        ans=0
        for i in l1 :
            ans+=(((i*(i+1))//2)%mod)
        return int(ans)


        