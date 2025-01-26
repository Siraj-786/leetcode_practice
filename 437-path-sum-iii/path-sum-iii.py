# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        d=defaultdict(int)
        d[0]=1
        ans=0 


        def recurse(root,k): 
            nonlocal d,ans 
            if not root :
                return 
            k+=root.val 
            if k-targetSum in d :
                ans+=d[k-targetSum] 
            d[k]+=1 

            recurse(root.left,k)
            recurse(root.right,k)
            d[k]-=1 
            if d[k]==0 :
                del d[k]
        recurse(root,0)
        return ans 


        