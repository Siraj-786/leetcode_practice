class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        new_min=[]
        new_max=[]
        
        for ele in arrays:
            new_min.append(min(ele))
            new_max.append(max(ele))
        ans=float("-inf")
        p=new_max.copy()
        p.sort()
        # print(p)
        for i in range(len(p)):
            ind=bisect.bisect_left(p,new_max[i])
            # print(p,ind,new_max[i])
            t=p.pop(ind)
            # print("a",p)
            ans=max(ans,p[-1]-new_min[i])
            bisect.insort(p,new_max[i])
        return ans