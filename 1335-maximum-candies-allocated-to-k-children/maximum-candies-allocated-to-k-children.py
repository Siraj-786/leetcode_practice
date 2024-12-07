class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies)<k :
            return 0 

        def no_of_piles(arr,v):
            c=0 
            for i in range(len(arr)):
                c+=math.floor(arr[i]/v)
            return c 

        l,r=1,10**9
        while l<=r :
            m=(l+r)//2
            a,b=l,r 
            if no_of_piles(candies,m)>=k :
                l=m +1
            else :
                r=m-1 
            if l==a and r==b :
                break 
        return r 

        