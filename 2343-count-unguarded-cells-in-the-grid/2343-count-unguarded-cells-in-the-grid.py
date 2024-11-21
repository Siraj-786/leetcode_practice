class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        left=[[0]*n for i in range(m)] 
        right=[[0]*n for i in range(m)] 
        up=[[0]*n for i in range(m)] 
        down=[[0]*n for i in range(m)] 



        for ele in guards :
            left[ele[0]][ele[1]]="g"
            right[ele[0]][ele[1]]="g"
            up[ele[0]][ele[1]]="g"
            down[ele[0]][ele[1]]="g"


        for ele in walls :
            left[ele[0]][ele[1]]="w"
            right[ele[0]][ele[1]]="w"
            up[ele[0]][ele[1]]="w"
            down[ele[0]][ele[1]]="w"
        # left flow 
        for i in range(m) :
            f=0
            for j in range(n):
                if left[i][j]=="w" :
                    f=0 
                    continue
                if left[i][j]=="g" :
                    f=1
                    continue
                left[i][j]=f 
        # right 
        for i in range(m):
            f=0 
            for j in range(n-1,-1,-1):
                if right[i][j]=="w" :
                    f=0 
                    continue 
                if right[i][j]=="g" :
                    f=1 
                    continue 
                right[i][j]=f 
        # up 
        for j in range(n):
            f=0 
            for i in range(m-1,-1,-1):
                if up[i][j]=="w" :
                    f=0 
                    continue 
                if up[i][j]=="g" :
                    f=1 
                    continue 
                up[i][j]=f 
        # down 

        for j in range(n):
            f=0 
            for i in range(m):
                if down[i][j]=="w" :
                    f=0 
                    continue 
                if down[i][j]=="g" :
                    f=1 
                    continue 
                down[i][j]=f
        ans=0
        for j in range(n) :
            for i in range(m) :
                if left[i][j]==0 and right[i][j]==0 and up[i][j]==0 and down[i][j]==0 :
                    ans+=1 

        # print(left)
        # print(right)
        # print(up)
        # print(down)
        return ans 






        

        