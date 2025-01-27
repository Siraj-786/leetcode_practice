class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def verify(k):
            ans=0 
            for ele in piles :
                ans+=math.ceil(ele/k)
            return ans 

        l=1 
        r=sum(piles)
        while l<r :
            mid=(l+r)//2 
            if verify(mid)<=h :
                r=mid 
            else :
                l=mid+1 
        return l 
        