class union_find  :


    def __init__(self,size):
        self.parent=list(range(size))
        self.rank=[0]*size


    def find(self,x) :
        if self.parent[x]!=x  :
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]

    
    def union(self,x,y):
        parent_x=self.find(x)
        parent_y=self.find(y)


        if self.rank[parent_x]>self.rank[parent_y] :
            self.parent[parent_y]=parent_x
        elif self.rank[parent_x]<self.rank[parent_y] :
            self.parent[parent_x]=parent_y
        else :
            self.parent[parent_x]=parent_y 
            self.rank[parent_y]+=1  

    



class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        size=len(grid)*len(grid[0])
        dsu=union_find(size)


        def index(r,c):
            return r*len(grid[0])+c

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1" :
                    for x,y in [(0,1),(0,-1),(1,0),(-1,0)]:
                        nr,nc=i+x,j+y 
                        if 0<=nr<len(grid) and 0<=nc<len(grid[0]) and grid[nr][nc]=="1" :
                            dsu.union(index(i,j),index(nr,nc))
        s=set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1" :
                    s.add(dsu.find(index(i,j)))
        return len(s)

        