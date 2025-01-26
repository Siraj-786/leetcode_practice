# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        d=defaultdict(int)


        def recurse(root,l):
            nonlocal d 
            if not root :
                return 
            if l not in d :
                d[l]=root.val
            if root.right :
                recurse(root.right,l+1)
            if root.left :
                recurse(root.left,l+1)   
        recurse(root,0)
        return [d[i] for i in range(len(d))]         
        