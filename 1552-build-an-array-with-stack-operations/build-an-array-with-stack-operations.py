class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        k=0 
        ans=[]
        ind=0
        while k<target[-1]:
            k+=1
            if target[ind]==k :
                ans.append("Push")
                ind+=1 
            else :
                ans.append("Push")
                ans.append("Pop")
        return ans

        