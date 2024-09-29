class Solution:
    def totalNQueens(self, n: int) -> int:
        c=0


        def verify(coord):
            x,y=coord[-1]
            if len(coord)==1 :
                return True 
            for i in range(len(coord)-1):
                p,q=coord[i]
                if p==x or q==y or abs(x-p)==abs(y-q) :
                    return False 
            return True 
        def recurse(lis,i):
            nonlocal c 
            if i==n :
                c+=1 
                return 
            for j in range(n):
                lis.append([i,j])
                if verify(lis):
                    recurse(lis,i+1)
                lis.pop(-1)
        recurse([],0)
        return c

        