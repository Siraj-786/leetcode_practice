class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        from collections import defaultdict
        
        # Step 1: Build Trie
        trie = {}
        for word in words:
            node = trie
            for letter in word:
                node = node.setdefault(letter, {})
            node["*"] = word

        n, m = len(board), len(board[0])
        ans = set()
        
        def backtrack(x, y, node):
            letter = board[x][y]
            curr_node = node[letter]

            word_match = curr_node.pop("*", False)
            if word_match:
                ans.add(word_match)
            
            board[x][y] = "#"
            for i, j in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                if 0 <= i < n and 0 <= j < m and board[i][j] in curr_node:
                    backtrack(i, j, curr_node)
            
            board[x][y] = letter
            
            if not curr_node:
                node.pop(letter)

        # Step 2: Search words using backtracking
        for i in range(n):
            for j in range(m):
                if board[i][j] in trie:
                    backtrack(i, j, trie)
        
        return list(ans)
