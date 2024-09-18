from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        new_t = {}
        def insert(word):
            curr = new_t
            for c in word:
                if c in curr:
                    curr = curr[c]
                else:
                    curr[c] = {}
                    curr = curr[c]
            curr["*"] = True
        
        for ele in strs:
            insert(ele)
        
        def find_prefix(root, ans):
            if len(root) != 1 or "*" in root:
                return ans
            for k in root:
                if k != "*":
                    return find_prefix(root[k], ans + k)
        
        return find_prefix(new_t, "")
