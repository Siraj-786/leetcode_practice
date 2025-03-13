class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:

        def check(k):
            counts=[0 for i in range((len(nums)+1))]
            # print(counts)
            for i in range(k):
                # print(queries[i][0])
                # print(queries[i][1])
                # print(queries[i][2])
                counts[queries[i][0]]+=queries[i][2]
                counts[queries[i][1]+1]-=queries[i][2]
            pre_counts=[counts[0]]
            for i in range(1,len(counts)):
                counts[i]=counts[i-1]+counts[i]
            # print(counts)
            for i in range(len(nums)):
                if nums[i]>counts[i]:
                    return False 
            # print(k,True )
            return True 
        i=0
        j=len(queries)
        flag=1
        ans=-1
        while i<=j  :
            mid=(i+j)//2 
            # print(mid)
            if check(mid) :
                j=mid-1
                ans=mid
                flag=0 
            else :
                i=mid+1
            # print(i,j)
        return ans 
        

        
        