from collections import defaultdict
from typing import List

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        
        # Create a trie structure
        trie = defaultdict(dict)

        # Function to insert a word into the trie
        def insert(word: str) -> None:
            curr = trie
            for char in word:
                if char not in curr:
                    curr[char] = defaultdict(dict)
                curr = curr[char]
            curr["*"] = True  # Mark the end of a word

        # Insert each word into the trie in reverse order
        for word in words:
            insert(word[::-1])

        ans = []
        
        # Check each word to see if it can be formed by concatenating other words
        for word in words:
            dp = [0] * (len(word) + 1)
            dp[0] = 1  # Initialize the empty string case
            
            for i in range(len(word)):
                curr = trie
                for j in range(i, -1, -1):  # Check prefixes from i to 0
                    if word[j] in curr:
                        curr = curr[word[j]]
                        if "*" in curr and dp[j] != 0:
                            dp[i + 1] = max(dp[i + 1], 1 + dp[j - 1])
                    else:
                        break  # Stop if the character is not found
            
            # We need at least two words to form a concatenated word
            if dp[-1] > 1:
                ans.append(word)

        return ans
