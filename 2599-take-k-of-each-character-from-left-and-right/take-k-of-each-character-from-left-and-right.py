class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        if s.count("a")<k or s.count("b")<k or s.count("c")<k :
            return -1
        if k==0 :
            return 0
        sa=[0]
        sb=[0]
        sc=[0]
        a=0
        b=0
        c=0
        for i in range(len(s)):
            if s[i]=="a" :
                a+=1 
            if s[i]=="b" :
                b+=1 
            if s[i]=="c" :
                c+=1 
            sa.append(a)
            sb.append(b)
            sc.append(c)
        da=defaultdict(int)
        db=defaultdict(int)
        dc=defaultdict(int)
        s=s[::-1]
        a=0
        b=0
        c=0
        da[0]=0
        db[0]=0
        dc[0]=0
        for i in range(len(s)):
            if s[i] =="a" :
                a+=1 
            if s[i]=="b" :
                b+=1 
            if s[i]=="c" :
                c+=1 
            if a not in da :
                da[a]=i+1
            if b not in db :
                db[b]=i+1
            if c not in dc :
                dc[c]=i+1
        min_ans=float("inf")
        for i in range(len(sa)):
            na,nb,nc=max(k-sa[i],0),max(k-sb[i],0),max(k-sc[i],0)
            
            min_ans=min(min_ans,max(da[na],db[nb],dc[nc])+i)
            # print(min_ans,na,nb,nc,da[na],db[nb],dc[nc])
        return min_ans
            

        