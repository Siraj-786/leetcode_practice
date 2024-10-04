class Solution:
    def minWindow(self, s: str, t: str) -> str:
        c=Counter(t)
        d=defaultdict(list)
        for i in range(len(s)):
            d[s[i]].append(i)
        ans=s
        up=0
        for i in range(len(s)):
            min_j=-1 
            f=True
            for k in c :
                if len(d[k])<c[k] :
                    f=False
                    continue
                else :
                    min_j=max(min_j,d[k][c[k]-1])
            for k in d :
                if d[k] :
                    if d[k][0]==i :
                        d[k].pop(0)
            if not f :
                continue
            l=min_j-i+1
            up=1
            if len(ans)>l :
                ans=s[i:min_j+1]
        if not up :
            return ""
        return ans 



        