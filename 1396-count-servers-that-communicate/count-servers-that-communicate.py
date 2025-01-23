class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        indices=[]
        di=defaultdict(list)
        dj=defaultdict(list)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1 :
                    indices.append((i,j))
                    di[i].append((i,j))
                    dj[j].append((i,j))
        visited=set()


        counts=defaultdict(int)


        while indices :
            p=indices.pop(0)
            if p not in visited :
                c=1
                h=p
                visited.add((p[0],p[1]))
                q=[p]
                while q :
                    p=q.pop(0)
                    for ele in di[p[0]] :
                        if ele not in visited :
                            visited.add(ele)
                            q.append(ele)
                            c+=1 
                    for ele in dj[p[1]]:
                        if ele not in visited :
                            visited.add(ele)
                            q.append(ele)
                            c+=1 
                counts[h]=c
        return sum([counts[i] for i in counts if counts[i]>1])
                
                

        