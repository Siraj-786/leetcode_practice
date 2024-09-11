class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        k=start^goal
        t=bin(k)[2:]
        return t.count("1")
        