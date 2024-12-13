# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:



        def recurse(root,parent):
            nonlocal ans
            if not root :
                return 0 

            left=recurse(root.left,root.val)
            right=recurse(root.right,root.val)
            ans=max(ans,left+right)
            if root.val==parent :
                return max(left,right)+1 
            else :
                return 0 
        ans=0
        recurse(root,-1)
        return ans 




        