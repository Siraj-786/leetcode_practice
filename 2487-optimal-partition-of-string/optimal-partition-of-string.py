class Solution:
    def partitionString(self, s: str) -> int:
        curr=[]
        ans=0
        for i in range(len(s)):
            if s[i] not in curr :
                curr.append(s[i])
            else :
                curr=[s[i]]
                ans+=1 
            # print(curr,ans)
        if curr :
            ans+=1 
        return ans 
        