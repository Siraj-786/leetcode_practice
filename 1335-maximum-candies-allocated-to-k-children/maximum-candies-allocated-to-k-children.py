class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def can_give(size,k):
            c=0 
            for i in range(len(candies)):
                c+=candies[i]//size 
            if c>=k :
                return True 
            return False 

        i=0
        j=sum(candies)
        while i<j :
            mid=(i+j+1)//2
            if can_give(mid,k):
                i=mid
            else :
                j=mid-1
            print(i,mid,j)
        return i
        