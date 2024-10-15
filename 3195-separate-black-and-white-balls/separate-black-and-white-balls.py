class Solution:
    def minimumSteps(self, s: str) -> int:
        ans=0
        o=s.count("1")
        a1=0
        k=len(s)-1
        for i in range(o):
            a1+=k
            k-=1 
        a2=0
        for i in range(len(s)):
            if s[i]=="1" :
                a2+=i 
        return a1-a2


       