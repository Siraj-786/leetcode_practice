class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check_max(i, offset=0):
            k = 0
            while i - k >= 0 and i + k + offset < len(s) and s[i - k] == s[i + k + offset]:
                k += 1
            return 2 * k + offset - 1

        ans = ""
        max_len = 0
        for i in range(len(s)):
            for offset in (0, 1):
                r = check_max(i, offset)
                if r > max_len:
                    max_len = r
                    ans = s[i - (r - offset) // 2 : i + r // 2 + 1]
                    
        return ans
