"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        arr=[]
        def rec(root):
            if not root :
                return 
            for child in root.children:
                rec(child)
            arr.append(root.val)
        rec(root)
        return arr
        