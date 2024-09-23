class Solution:
    def smallestSubsequence(self, s: str) -> str:

        stack=[]

        d=defaultdict(int)
        for i in range(len(s)):
            d[s[i]]=i 

        for i in range(len(s)):
            if s[i] not in stack :
                while stack and s[i]<stack[-1] and i<d[stack[-1]] :
                    stack.pop(-1)
                stack.append(s[i])
        return "".join(stack)

        