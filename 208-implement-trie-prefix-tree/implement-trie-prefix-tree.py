class Trie:

    def __init__(self):
        self.d={}
        

    def insert(self, word: str) -> None:
        curr=self.d 
        for ele in word :
            if  ele not in curr :
                curr[ele]={}
                curr=curr[ele]
            else :
                curr=curr[ele]
        curr["*"]=True 

            
        

    def search(self, word: str) -> bool:
        curr=self.d
        for ele in word :
            if ele not in curr :
                return False 
            else :
                curr=curr[ele]
        if "*" in curr :
            return True 
        return False 
        

    def startsWith(self, prefix: str) -> bool:
        curr=self.d
        for ele in prefix :
            if ele not in curr :
                return False 
            else :
                curr=curr[ele]
        # if "*" in curr :
        return True 

        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)