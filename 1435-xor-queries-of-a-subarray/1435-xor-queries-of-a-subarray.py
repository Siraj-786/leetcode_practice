class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        l1=[arr[0]]
        ans=[]
        for i in range(1,len(arr)):
            l1.append(l1[-1]^arr[i])
        for ele in queries:
            if (ele[0])<=0 :
                ans.append(l1[ele[1]])
            else :
                ans.append(l1[ele[0]-1]^l1[ele[1]])
        return ans