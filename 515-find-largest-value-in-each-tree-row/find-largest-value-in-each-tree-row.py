# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root :
            return []
        ans=[root.val]
        q=[root]
        while q :
            maxi=float("-inf")
            new_q=[]
            for ele in q :
                if ele.left :
                    new_q.append(ele.left)
                    maxi=max(maxi,ele.left.val)
                if ele.right :
                    new_q.append(ele.right)
                    maxi=max(maxi,ele.right.val)
            ans.append(maxi)
            q=new_q 
        return ans[:-1
        ]
        