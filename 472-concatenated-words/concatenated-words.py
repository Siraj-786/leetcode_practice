class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words.sort()
        trie=defaultdict()
        def insert(word):
            curr=trie 
            f=False 
            for w in word :
                if w in curr :
                    curr=curr[w]
                    f=True

                else :
                    curr[w]=defaultdict()
                    curr=curr[w]
            curr["*"]=f
        for c in words :
            insert(c[::-1])
        ans=[]


        for ele in words :
            dp=[1]+[0]*len(ele)
            for i in range(len(ele)):
                curr=trie 
                for j in range(i,-1,-1):
                    if ele[j] in curr :
                        curr=curr[ele[j]]
                        if "*" in curr and dp[j]!=0 :
                            dp[i+1]=max(dp[i+1],1+dp[j-1])
                    else :
                        break 
            print(dp)
            if dp[-1]>1 :
                ans.append(ele)




        return ans 
                        
                        




        