# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # ans=[]



        def recurse(root):
            # nonlocal ans
            if not root :
                return 
            if root.val==val :
                return root
            s=recurse(root.left) 
            if s :
                return s
            
            i=recurse(root.right)
            if i :
                return i 
                # return recurse(root.right)
            return 
        return recurse(root)
            
            

        