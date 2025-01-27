class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        d=defaultdict(list)
        for ele in prerequisites :
            d[ele[0]].append(ele[1])
        


        v=[set() for i in range(numCourses)]
        for i in range(numCourses):
            v[i].add(i)
            q=[i]
            while q :
                for ele in d[q.pop(0)] :
                    if ele not in v[i] :
                        v[i].add(ele)
                        q.append(ele)
        ans=[]
        print(v)
        for q in queries :
            x,y=q 

            if v[x] and y in v[x] :
                ans.append(True)
            else :
                ans.append(False )
        return ans 

        