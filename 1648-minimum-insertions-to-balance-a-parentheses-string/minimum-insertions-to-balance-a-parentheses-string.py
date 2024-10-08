class Solution:
    def minInsertions(self, s: str) -> int:
        q=[]
        ans=0
        i=0
        while i<len(s):
            if s[i]=="(":
                q.append("a")
                i+=1
            else :
                if i+1<len(s) :
                    if s[i]==s[i+1] :
                        i+=2
                    else :
                        ans+=1
                        i+=1
                    q.append("b")
                else :
                    i+=1 
                    q.append("b")
                    ans+=1
        print(ans)
        a=[]
        b=[]
        for i in range(len(q)):
            if q[i]=="a" :
                a.append(i)
            else :
                b.append(i)
        print(q,a,b)
        while a or b :
            if a and b :
                if a[0]<b[0] :
                    a.pop(0)
                    b.pop(0)
                else :
                    ans+=1 
                    b.pop(0)
            elif a :
                a.pop(0)
                ans+=2
            else :
                b.pop(0)
                ans+=1
        return ans







        