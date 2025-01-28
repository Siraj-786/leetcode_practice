class union_find :
    def __init__(self,size):
        self.parent=list(range(size))
        self.rank=[0]*(size)


    def find(self,x):
        if self.parent[x]!=x :
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
    def findMaxFish(self, grid: List[List[int]]) -> int:


        def index(x,y):
            return x*len(grid[0])+y 

        dsu=union_find(len(grid)*len(grid[0]))


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                for (x,y) in [(0,1),(0,-1),(1,0),(-1,0)]:
                    if 0<=(i+x)<len(grid) and 0<=(j+y)<len(grid[0]) and grid[i+x][j+y] and grid[i][j]:
                        if dsu.find(index(i+x,j+y))!=dsu.find(index(i,j)):
                            dsu.union(index(i+x,j+y),index(i,j))
        d=defaultdict(int)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]!=0 :
                    d[dsu.find(index(i,j))]+=grid[i][j]
        # return 0
        print(dsu.parent)
                    
        maxi=0 
        for ele in d :
            maxi=max(maxi,d[ele])
        return maxi 

        
        