# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        has=defaultdict(int)
        if not root :
            return []
        l1=[root]
        has[root.val]+=1
        while l1 :
            t=[]
            for i in l1 :
                if i.left :
                    t.append(i.left)
                    has[i.left.val]+=1
                if i.right :
                    t.append(i.right)
                    has[i.right.val]+=1
            l1=t
        maxi=max(i for i in has.values())
        ans=[]
        for i in has :
            if has[i]==maxi :
                ans.append(i)
        return ans  
                
                


        