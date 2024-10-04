class Solution:
    def partition(self, s: str) -> List[List[str]]:



        ans=[]
        def verify(arr):
            for ele in arr :
                if ele!=ele[::-1] :
                    return False 
            return True 

        def rec(arr,i):
            if i==len(s) :
                if verify(arr):
                    ans.append(arr.copy())
                return 
            # include 
            if arr :
                last=arr[-1]
                arr[-1]=last+s[i]
                rec(arr,i+1)
                arr[-1]=last
            arr.append(s[i])
            rec(arr,i+1)
            arr.pop(-1)
        rec([],0)
        return ans
