class Solution:
    def minimumDeletions(self, s: str) -> int:


        ans=float("inf")
        prefix=[0]
        for i in range(len(s)):
            if s[i]=="b" :
                prefix.append(prefix[-1]+1)
            else :
                prefix.append(prefix[-1])
        # print(prefix)

        suffix=[0]
        for i in range(len(s)-1,-1,-1):
            if s[i]=="a":

                suffix.append(suffix[-1]+1)
            else :
                suffix.append(suffix[-1])
        suffix=suffix[::-1]
        # print(suffix)
        for i in range(len(s)+1):
            ans=min(ans,prefix[i]+suffix[i])
        return ans
        