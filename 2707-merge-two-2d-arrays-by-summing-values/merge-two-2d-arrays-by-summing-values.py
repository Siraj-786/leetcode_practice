class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:

        d=defaultdict(int)
        for ele in nums1:
            d[ele[0]]+=ele[1]
        for ele in nums2 :
            d[ele[0]]+=ele[1]
        l1=[[i,d[i]] for i in sorted(list(d.keys()))]
        return l1