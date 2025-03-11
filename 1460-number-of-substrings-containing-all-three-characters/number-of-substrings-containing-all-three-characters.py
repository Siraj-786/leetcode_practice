class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ans=0 

        pre_a=[-1]
        pre_b=[-1]
        pre_c=[-1]
        for i in range(len(s)):
            if s[i]=="a" :
                pre_a.append(i)
            else :
                pre_a.append(pre_a[-1])

            if s[i]=="b" :
                pre_b.append(i)
            else :
                pre_b.append(pre_b[-1])
            if s[i]=="c" :
                pre_c.append(i)
            else :
                pre_c.append(pre_c[-1])
        print(pre_a)
        print(pre_b)
        print(pre_c)
        ans=0
        for i in range(len(s)) :
            if pre_a[i+1]!=-1 and pre_b[i+1]!=-1 and pre_c[i+1]!=-1 :
                if s[i]=="a" :
                    mini=min(pre_b[i+1],pre_c[i+1])
                    ans+=(mini+1) 

                if s[i]=="b" :
                    mini=min(pre_a[i+1],pre_c[i+1])
                    ans+=(mini+1) 

                if s[i]=="c" :
                    mini=min(pre_a[i+1],pre_b[i+1])
                    ans+=(mini+1) 
        return ans 
                


        