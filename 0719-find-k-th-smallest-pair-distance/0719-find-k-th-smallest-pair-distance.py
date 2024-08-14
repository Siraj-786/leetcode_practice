class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def count(d):
            # print(nums)
            c=0
            for i in range(len(nums)):
                to=nums[i]+d
                ind=bisect.bisect(nums,to)
                # print(i,ind,to)
                c+=(ind-i-1)
            return c 
        nums.sort()
        i=0
        j=10000000
        while i<=j :
            mid=(i+j)//2
            print(mid,count(mid))
            if count(mid)>=k:
                j=mid-1
            else :
                i=mid+1
        return i
        print(count(5))
        return 9

        