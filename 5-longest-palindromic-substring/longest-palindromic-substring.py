class Solution:
    def longestPalindrome(self, s: str) -> str:
        # odd
        def check_max(i):
            j=i 
            k=1
            while j-k>=0 and j+k<len(s) :
                if s[j-k]==s[j+k] :
                    k+=1
                else :
                    break 
            return 1+2*(k-1)
        ans=""
        max_len=0
        for i in range(len(s)):
            r=check_max(i)
            if r>max_len :
                max_len=r 
                ans=s[i-r//2:i+1+r//2]
        
        def check_max1(i):
            j=i 
            k=1
            while j-k>=0 and j+k+1<len(s) :
                if s[j-k]==s[j+k+1] :
                    k+=1
                else :
                    break 
            return 2*(k)
        for i in range(len(s)-1):
            if s[i]==s[i+1] :
                r=check_max1(i)
                if r>max_len :
                    max_len=r 
                    ans=s[i-(r-2)//2:i+1+r//2]
        return ans


        

        