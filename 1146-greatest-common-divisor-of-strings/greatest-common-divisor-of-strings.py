class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        a=str1 
        b=str2

        def check(a,b,k):
            l1=len(a)//len(k)
            l2=len(b)//len(k)
            if l1*k==a and l2*k==b :
                return True 
            return False 
        ans=""
        for i in range(min(len(a),len(b))):
            if a[i]==b[i] :
                if check(a,b,a[0:i+1]) :
                    ans=a[0:i+1]
                # else :
                #     break 
            else :
                break 
        return ans 



        