class Solution:
    def shortestPalindrome(self, s: str) -> str:
        for i in range(len(s)):
            # print(s[len(s)-i::-1])
            if s[0:len(s)-i]==s[0:len(s)-i][::-1] :
                # print(s[0:len(s)-i])
                return s[len(s)-(i):][::-1]+s
        return s
