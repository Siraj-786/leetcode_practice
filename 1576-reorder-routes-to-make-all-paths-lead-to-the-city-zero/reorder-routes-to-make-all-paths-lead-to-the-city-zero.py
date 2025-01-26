class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:

        d=defaultdict(list)
        s=set()
        for ele in connections :
            s.add(tuple(ele))
        for ele in connections :
            d[ele[0]].append(ele[1])
            d[ele[1]].append(ele[0])
        q=[0]
        visited=set()
        visited.add(0)
        ans=0
        while q :
            p=q.pop(0)
            for ele in d[p] :
                if ele not in visited :
                    visited.add(ele)
                    q.append(ele)
                    if (p,ele) in s :
                        ans+=1 
        return ans 



            

        