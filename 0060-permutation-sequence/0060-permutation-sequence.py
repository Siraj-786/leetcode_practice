class Solution:
    p = []
    s = set()

    def getPermutation(self, n: int, k: int) -> str:
        self.p.clear()  # Clear previous results
        self.s.clear()  # Clear previous set

        def recurse(lis):
            if len(lis) == n:
                self.p.append(lis.copy())
                return

            for i in range(1, n + 1):
                if i not in self.s:
                    lis.append(i)
                    self.s.add(i)
                    recurse(lis)
                    lis.pop(-1)
                    self.s.remove(i)

        recurse([])
        return "".join(str(i) for i in self.p[k - 1])
