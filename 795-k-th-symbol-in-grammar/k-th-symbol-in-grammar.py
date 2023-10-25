class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 0:
            return 0

        def bit_place(num, left, right, k1):
            m = (left + right) // 2
            if k1 == n:
                return num
            if left <= k <= m:
                if num[0] == '0':
                    return bit_place("0", left, m, k1 + 1)
                else:
                    return  bit_place("1", left, m, k1 + 1)

            else:
                if num[-1] == "0":
                    return bit_place("1", m + 1, right, k1 + 1)
                else:
                    return bit_place("0", m + 1, right, k1 + 1)

        return int(bit_place("0", 1, 2 ** (n - 1), 1))