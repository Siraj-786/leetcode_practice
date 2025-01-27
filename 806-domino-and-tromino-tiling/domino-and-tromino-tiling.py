class Solution:
    def numTilings(self, n: int) -> int:
        f={0:1,1:1}
        b={1:0}
        t={1:0}
        for i in range(2,n+1) :
            f[i]=f[i-1]+f[i-2]+t[i-1]+b[i-1]
            t[i]=f[i-2]+b[i-1]
            b[i]=f[i-2]+t[i-1]
        return f[n]%(10**9+7)
