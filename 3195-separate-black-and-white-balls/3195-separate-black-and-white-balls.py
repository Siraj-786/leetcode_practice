class Solution:
    def minimumSteps(self, s: str) -> int:
        ans=0
        o=s.count("1")
        a1=[]
        k=len(s)-1
        for i in range(o):
            a1.append(k)
            k-=1 
        a2=[]
        for i in range(len(s)):
            if s[i]=="1" :
                a2.append(i)
        return sum(a1)-sum(a2)


       