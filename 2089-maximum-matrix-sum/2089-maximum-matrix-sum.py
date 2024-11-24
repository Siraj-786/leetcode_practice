class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        mini=float("inf")
        neg=0
        z=0
        s=0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                mini=min(abs(matrix[i][j]),mini)
                s+=abs(matrix[i][j])
                if matrix[i][j]==0 :
                    z+=1
                if matrix[i][j]<0 :
                    neg+=1 
        if z :
            return s
        print(mini,s,neg)
        if neg&1 :
            return s-2*mini 
        else :
            return s 
        