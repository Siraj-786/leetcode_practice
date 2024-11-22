class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:

        l1=[]
        def same(s1,s2):
            # k=0 
            for i in range(len(s1)) :
                if s1[i]!=s2[i] :
                    return False 
            return True 
        def oppo(s1,s2):
            for i in range(len(s1)) :
                if s1[i]==s2[i] :
                    return False 
            return True 
        maxi=0
        for i in range(len(matrix)):
            p=0 
            for j in range(len(matrix)) :
                if same(matrix[i],matrix[j]) or oppo(matrix[i],matrix[j]) :
                    p+=1 
            maxi=max(maxi,p)
            
        return maxi 
        