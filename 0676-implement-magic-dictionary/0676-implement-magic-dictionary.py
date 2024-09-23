class MagicDictionary:

    def __init__(self):
        self.trie=defaultdict()
        

    def buildDict(self, dictionary: List[str]) -> None:

        def insert(word):
            curr=self.trie
            for c in word :
                if c in curr :
                    curr=curr[c]
                else :
                    curr[c]=defaultdict()
                    curr=curr[c]
            curr["*"]=True 
        for w in dictionary:
            insert(w)
        
        

    def search(self, searchWord: str) -> bool:

        def dfs(root,s,i,no_of_change):
            if no_of_change>1 :
                return False 
            if i==len(s) :
                if no_of_change==1 :
                    if "*" in root :
                        return True 
                return False 
            for ele in root :
                if ele=="*":
                    continue
                if ele==s[i] :
                    if  dfs(root[ele],s,i+1,no_of_change) :
                        return True 
                else :
                    if dfs(root[ele],s,i+1,no_of_change+1) :
                        return True 
            return False 
        return dfs(self.trie,searchWord,0,0)
                    

            # for ele in root :


        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)