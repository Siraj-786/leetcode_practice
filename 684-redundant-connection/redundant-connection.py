
class union_find  :
    def __init__(self,size):
        self.parent=list(range(size))
        self.rank=[0]*size

    
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
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        ans=[]

        maxi=[]
        for ele in edges :
            maxi.append(ele[0])
            maxi.append(ele[1])
        maxi=max(maxi)
        dsu=union_find(maxi+1)
        for edge in edges :
            x,y=edge
            if dsu.find(x)!=dsu.find(y) :
                dsu.union(x,y)
            else :
                ans.append(edge)
        return ans[0]
        