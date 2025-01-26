



class find_union :

    def __init__(self,size):
        self.parent=list(range(size))
        self.rank=[0]*size


    def find(self,x):
        if self.parent[x]!=x :
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    

    def union (self,x,y):
        parent_x=self.parent[x]
        parent_y=self.parent[y]

        if self.rank[parent_x]>self.rank[parent_y] :
            self.parent[parent_y]=parent_x
        elif self.rank[parent_x]<self.rank[parent_y] :
            self.parent[parent_x]=parent_y
        else  :
            self.parent[parent_x]=parent_y
            self.rank[parent_y]+=1 
    


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:


        dsu=find_union(len(isConnected))

        n=len(isConnected)
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j]==1 and dsu.find(i)!=dsu.find(j) :
                    n-=1
                    dsu.union(i,j)
        return n  




        