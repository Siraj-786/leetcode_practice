class Solution:    
    def nthUglyNumber(self, n: int) -> int:
        l1=set()    
        l1.add(1)
        while len(l1)<=5690:
            for ele in list(l1):
                l1.add(ele*2)
                l1.add(ele*3)
                l1.add(ele*5)
        l1=sorted(list(l1))
        return l1[n-1]