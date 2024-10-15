class Solution:
    def minimumSteps(self, s: str) -> int:
        z = s.count("0")
        if (z * "0" + (len(s) - z) * "1") == s:
            return 0
        one_index = []
        for i in range(len(s)):
            if s[i] == "1":
                one_index.append(i)
        ans=0
        for i in range(z,len(s)):
            ans+=(i-one_index[i-z])
        return ans