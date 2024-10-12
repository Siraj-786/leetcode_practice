class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:


        maxi_num=max(intervals[i][1] for i in range(len(intervals)))
        start=[0]*(maxi_num+1) 
        end=[0]*(maxi_num+1)
        for ele in intervals :
            start[ele[0]]+=1 
            end[ele[1]]-=1 
        # print(start)
        # print(end)
        ans=0
        curr=0
        for i in range(maxi_num+1):
            curr+=start[i]
            # print(curr)
            ans=max(ans,curr)
            curr+=end[i]
        return ans 
        