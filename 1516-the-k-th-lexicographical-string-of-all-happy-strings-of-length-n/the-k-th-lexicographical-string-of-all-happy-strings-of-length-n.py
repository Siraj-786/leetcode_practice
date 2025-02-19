class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        ans=""
        counter=0 
        poss=["a","b","c"]
        def recurse(curr,i,lenn):
            nonlocal ans
            nonlocal counter
            if len(curr)>lenn :
                return 
             
            if len(curr)==lenn :
                counter+=1 
                 
            if len(curr)==lenn and counter==k: 
                ans=curr 
                return
            for i in range(3):
                if curr :
                    if curr[-1]!=poss[i] :
                        curr+=poss[i]
                        recurse(curr,i,lenn)
                        curr=curr[0:-1]
                else :
                    curr=poss[i]
                    recurse(curr,i,lenn)
                    curr=""
        recurse("",0,n)
        return ans 


        