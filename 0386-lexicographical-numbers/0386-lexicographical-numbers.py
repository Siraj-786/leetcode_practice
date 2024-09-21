from sortedcontainers import SortedDict
from typing import List

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        trie = SortedDict()

        def insert(word):
            curr = trie
            for c in word:
                if c in curr:
                    curr = curr[c]
                else:
                    curr[c] = SortedDict()
                    curr = curr[c]
            curr["*"] = True

        for i in range(1, n + 1):
            insert(str(i))

        ans=[]
        def get_ans(root,k):
            if "*" in root :
                ans.append(int(k))
            for ele in root :
                if ele !="*" :
                    get_ans(root[ele],k+ele)
        get_ans(trie,"")
        return ans

