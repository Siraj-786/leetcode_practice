class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:

        d=defaultdict(int)
        for ele in items :
            d[ele[0]]=max(d[ele[0]],ele[1])
        s=list(d.keys()) 
        s.sort()
        val=[]
        for i in  s :
            val.append(d[i])
        prefix=[val[0]]
        for i in range(1,len(val)):
            prefix.append(max(prefix[-1],val[i]))
        # print(prefix)
        ans=[]
        for i in range(len(queries)):
            ind=bisect.bisect_right(s,queries[i])
            if ind==0 :
                ans.append(0)
            else :
                ans.append(prefix[ind-1])
        return ans 
        