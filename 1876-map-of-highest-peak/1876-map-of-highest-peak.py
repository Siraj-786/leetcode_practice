class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        poss=[]
        for i in range(len(isWater)):
            for j in range(len(isWater[0])):
                if isWater[i][j]==1 :
                    poss.append((i,j))
        visited=set()
        ans=isWater.copy()
        n,m=len(isWater),len(isWater[0])

        levels=[i for i in poss]
        for ele in poss :
            visited.add(ele)
        l=0
        # print(levels)
        while levels :
            new=[]
            for ele in levels:
                # print(ele[0],ele[1],ans)
                ans[ele[0]][ele[1]]=l
                a,b=ele[0],ele[1]
                for i,j in [(1,0),(0,1),(-1,0),(0,-1)] :
                    if 0<=(a+i)<n and 0<=(b+j)<m  and (a+i,b+j) not in visited:
                        visited.add((a+i,b+j))
                        new.append((a+i,b+j))
            l+=1 
            levels=new 
            # print("sss")
        return ans 






        