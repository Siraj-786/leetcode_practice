class Trie:

    def __init__(self):
        self.trie={}
        

    def insert(self, word: str) -> None:

        curr=self.trie 
        for c in word :
            if c in curr :
                curr=curr[c]
            else :
                curr[c]={}
                curr=curr[c]
        curr["*"]=True 

        

    def search(self, word: str) -> bool:
        curr=self.trie 

        for c in word :
            if c not in curr :
                return False
            # if curr[c]==True :
            #     return True  
            curr=curr[c]
        print(curr)
        if  "*" in curr :
            return True 
        return False 

        return True         

    def startsWith(self, prefix: str) -> bool:
        curr=self.trie 

        for c in prefix :
            if c not in curr :
                return False 
            curr=curr[c]
        return True 


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)