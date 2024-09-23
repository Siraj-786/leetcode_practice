from collections import defaultdict

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        trie = defaultdict(dict)
        
        def insert(word):
            curr = trie
            for c in word:
                if c not in curr:
                    curr[c] = {}
                curr = curr[c]
            if "*" in curr:
                curr["*"] += 1
            else:
                curr["*"] = 1

        for w in words:
            insert(w)

        freq_list = []

        def dfs(node, word):
            if "*" in node:
                freq_list.append((word, node["*"]))
            for c in sorted(node.keys()):  
                if c != "*":
                    dfs(node[c], word + c)
        
        dfs(trie, "")

        freq_list.sort(key=lambda x: (-x[1], x[0])) 

        return [word for word, freq in freq_list[:k]]
