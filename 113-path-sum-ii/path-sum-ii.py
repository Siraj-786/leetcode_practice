# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans=[]
        if not root :
            return []


        def dfs(arr,root):
            if not root.left  and not root.right  :
                arr.append(root.val) 
                if sum(arr)==targetSum :
                    ans.append(arr.copy())
                arr.pop(-1)
                return 
            if root.left :
                arr.append(root.val) 
                dfs(arr,root.left)
                arr.pop(-1)
            if root.right :
                arr.append(root.val) 
                dfs(arr,root.right)
                arr.pop(-1)
        dfs([],root)
        return ans

        