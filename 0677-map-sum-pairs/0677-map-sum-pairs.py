from collections import defaultdict

class MapSum:

    def __init__(self):
        self.trie = defaultdict(dict)
        

    def insert(self, key: str, val: int) -> None:
        curr = self.trie
        for c in key:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]
        curr['*'] = val
        

    def sum(self, prefix: str) -> int:

        # Find the node that matches the prefix
        curr = self.trie
        for c in prefix:
            if c not in curr:
                return 0  # Prefix does not exist in the trie
            curr = curr[c]
        
        # DFS to sum all values for this prefix
        def dfs(node):
            total = 0
            if '*' in node:
                total += node['*']
            for child in node:
                if child != '*':
                    total += dfs(node[child])
            return total
        
        return dfs(curr)


# Example Usage:
# obj = MapSum()
# obj.insert("apple", 3)
# print(obj.sum("ap"))  # Outputs 3
# obj.insert("app", 2)
# print(obj.sum("ap"))  # Outputs 5
