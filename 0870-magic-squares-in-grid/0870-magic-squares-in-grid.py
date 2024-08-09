class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:


        def for_matrix(mat): #[[],[],[]]
            r=[0,0,0]
            c=[0,0,0]
            d1=0
            d2=0
            s=set()
            for i in range(3):
                row_sum=0
                col_sum=0
                for j in range(3):
                    s.add(mat[i][j])
                    row_sum+=mat[i][j]
                    col_sum+=mat[j][i]
                    if i==j :
                        d1+=mat[i][j]
                        d2+=mat[i][2-j]
                
                    
                r[i]=row_sum
                c[i]=col_sum
            if r!=c or [15]*3!=r or [15]*3!=c or d1!=d2 or d1!=15 or d2!=15 :
                return False 
            

            # alt 
            for i in range(1,10):
                # print(i)
                if i not in s :
                    return False 
            # print(s)
            # print("grid",mat,d1,d2)
            return True 

        ans=0

        for i in range(len(grid)-2):
            for j in range(len(grid[0])-2):
                mat=[]
                for a in range(i,i+3):
                    l1=[]
                    for b in range(j,j+3):
                        l1.append(grid[a][b])
                    mat.append(l1)
                        
                print(mat)
                if for_matrix(mat):
                    ans+=1 
        return ans




        