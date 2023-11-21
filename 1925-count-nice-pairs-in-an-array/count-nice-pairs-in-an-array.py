class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        d = defaultdict(int)

        def reverse_int(n):
            rev = 0
            while n > 0:
                rev = rev * 10 + n % 10
                n = n // 10
            return rev

        for num in nums:
            d[num - reverse_int(num)] += 1
        ans = 0
        for key in d:
            ans += (d[key] * (d[key] - 1)) // 2
        return ans % (10 ** 9 + 7)