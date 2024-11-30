from collections import defaultdict
from typing import List

class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        adjacency = defaultdict(list)
        out_degree = defaultdict(int)
        in_degree = defaultdict(int)

        for start, end in pairs:
            adjacency[start].append([start, end])
            out_degree[start] += 1
            in_degree[end] += 1

        start_node = -1
        for node in out_degree:
            if out_degree[node] > in_degree[node]:
                start_node = node
                break

        if start_node == -1:
            start_node = pairs[0][0]

        result = []

        def dfs(node):
            while adjacency[node]:
                next_pair = adjacency[node].pop()
                dfs(next_pair[1])
                result.append(next_pair)

        dfs(start_node)

        return result[::-1]
