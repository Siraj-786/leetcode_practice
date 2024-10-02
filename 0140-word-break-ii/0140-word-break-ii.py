class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        trie=defaultdict()
        def insert(word):
            curr=trie 
            for c in word :
                if c in curr :
                    curr=curr[c]
                else :
                    curr[c]=defaultdict()
                    curr=curr[c]
            curr["*"]=True 
        for w in wordDict :
            insert(w)
        # print(trie)
        ans=[]
        def recurse(curr,sub,i):
            if i==len(s)  and "*" in curr:
                ans.append(sub)
                return 
            if i==len(s) :
                return 
            p=sub
            if "*" in curr and s[i] in trie :
                p+=" "
                recurse(trie[s[i]],p+s[i],i+1)

            q=sub
            if s[i] in curr :
                recurse(curr[s[i]],q+s[i],i+1)
            # r=sub
            # if s[i] in trie :
            #     recurse(trie[s[i]],r+s[i],i+1)
            return 
        recurse(trie,"",0)
        return ans


        