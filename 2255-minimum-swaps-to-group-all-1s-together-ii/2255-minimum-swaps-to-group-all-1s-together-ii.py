class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        
        def forele(ele,arr):
            c=arr.count(ele)
            k=c
            d=defaultdict(int)
            j=0
            for i in range(c):
                d[arr[i]]+=1
            mini=c-d[ele]
            # c-=1
            # print(d)
            while c<len(arr):
                d[arr[j]]-=1
                d[arr[c]]+=1 
                mini=min(mini,k-d[ele])
                c+=1 
                j+=1 
                # print(d)
            return mini
        return min(forele(0,nums),forele(1,nums))






        