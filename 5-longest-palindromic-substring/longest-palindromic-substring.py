class Solution:
    def longestPalindrome(self, s: str) -> str:
        # two pointers kind off 
        mini_len_found=1
        ans=s[0]
        def check_odd(p):
            a,b=p,p
            
            while a>0 and b<len(s)-1:
                a-=1 
                b+=1
                if s[a]!=s[b] :
                    a+=1 
                    b-=1 
                    break
            return s[a:b+1]
        def check_even(a,b):
            if s[a]!=s[b] :
                return s[a]
            
            while a>0 and b<len(s)-1 :
                a-=1
                b+=1 
                if s[a]!=s[b] :
                    a+=1
                    b-=1 
                    break
            return s[a:b+1]
        for i in range(len(s)-1):
            # for odd len 
            centre=i 
            ch_odd=check_odd(i)
            if len(ch_odd)>mini_len_found :
                mini_len_found=len(ch_odd)
                ans=ch_odd
            ch_even=check_even(i,i+1)
            print(ch_even)
            if len(ch_even)>mini_len_found :
                mini_len_found=len(ch_even)
                ans=ch_even 
        return ans



            

