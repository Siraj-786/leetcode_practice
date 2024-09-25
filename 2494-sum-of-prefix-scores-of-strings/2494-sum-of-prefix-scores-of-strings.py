class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:

        # single run and single submittion 
        # code by siraj 
        trie=defaultdict()
        def insert(word):
            curr=trie 
            for c in word :
                if c in curr :
                    p=curr[c]
                    p["*"]+=1
                    curr=curr[c]
                else :
                    curr[c]=defaultdict()
                    curr=curr[c]
                    curr["*"]=1
        for ele in words :
            insert(ele)
        ans=[]
        def get_ans(word):
            s=0
            curr=trie
            for c in word :
                curr=curr[c]
                s+=curr["*"]
            return s 
        for ele in words :
            ans.append(get_ans(ele))
        return ans 




        
        