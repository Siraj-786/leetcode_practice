class Solution:
    @cache
    def isScramble(self, s1: str, s2: str) -> bool:
        if s1 == s2: return True
        if Counter(s1) != Counter(s2): return False
        return any((self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:])) or
                   (self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i]))
                   for i in range(1, len(s1)))