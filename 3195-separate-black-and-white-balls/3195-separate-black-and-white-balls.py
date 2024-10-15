class Solution:
    def minimumSteps(self, s: str) -> int:
        a1=0
        a2=0
        k=len(s)-1
        for i in range(len(s)):
            if s[i]=="1":
                a1+=k
                k-=1 
                a2+=i 
        return a1-a2


       