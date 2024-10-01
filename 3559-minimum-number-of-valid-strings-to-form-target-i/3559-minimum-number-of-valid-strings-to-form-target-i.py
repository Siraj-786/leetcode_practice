from collections import defaultdict
from typing import List

class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        trie = defaultdict(dict)

        def insert(word):
            curr = trie
            for c in word:
                if c not in curr:
                    curr[c] = defaultdict(dict)
                curr = curr[c]
            curr["*"] = True
        
        # Insert all words into the trie
        for w in words:
            insert(w)
        
        # Initialize dp array to store minimum valid strings
        dp = [i + 1 for i in range(len(target))]
        target=target[::-1]
        dpt=[True]

        for i in range(len(target)):
            j = i
            curr = trie
            p=False
            
            while j >= 0 and target[j] in curr :
                
                # print(j, i)  # Debugging print
                if dpt[j]==True :
                    # print(j,i,"l")
                    p=True
                curr = curr[target[j]]
                dp[i] = min(dp[i], dp[j] + 1)
                j -= 1
            
            
            dp[i] = min(dp[i], dp[j] + 1)

            if j == -1:
                
                dp[i] = min(dp[i], 1)
            dpt.append(p)

            # print(dp)
        # print(dpt)
        if dpt[-1] :
              # Debugging print
            return dp[-1]
        return -1
        

        
