class Solution:
    def minimumPushes(self, word: str) -> int:
        k=1 
        f=0
        c=Counter(word)
        l1=list(c.values())
        
        l1.sort(reverse=True)
        print(l1)
        ans=0
        for ele in l1 :
            if f==8 :
                k+=1
                f=0 
            ans+=(ele*k)
            print(ans)
            f+=1 
            
        return ans 


        


        