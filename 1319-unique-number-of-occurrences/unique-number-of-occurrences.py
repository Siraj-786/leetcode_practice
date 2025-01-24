class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c=Counter(arr)
        s=[c[i] for i in c]
        if len(s)!=len(set(s)) :
            return False 
        return True 
        