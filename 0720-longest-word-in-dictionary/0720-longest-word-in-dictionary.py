from collections import defaultdict

class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = defaultdict(dict)

        def insert(word):
            curr = trie
            for c in word:
                if c not in curr:
                    curr[c] = defaultdict()
                curr = curr[c]
            curr["*"] = True  

        for w in words:
            insert(w)

        longest_word = ""

        def check(root, s):
            for i in range(len(s)):
                if s[i] not in root:
                    return False
                root = root[s[i]]
                if "*" not in root and i < len(s) - 1:  
                    return False
            return True
        for word in sorted(words): 
            if check(trie, word):
                if len(word) > len(longest_word):
                    longest_word = word

        return longest_word
