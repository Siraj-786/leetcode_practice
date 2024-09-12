class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        c=0


        def comp(s1,s2):
            for e in s2 :
                if e not in s1 :
                    return False 
            return True
        s1=set(allowed)
        for ele in words :
            if comp(s1,set(ele)):
                c+=1 

        return c
        