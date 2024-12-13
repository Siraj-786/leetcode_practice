# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        arr=[]
        def recurse(root):
            nonlocal arr
            if not root  :
                return 
            recurse(root.left)
            arr.append(root.val)
            recurse(root.right)
        recurse(root)
        # arr.append(-1)
        arr.insert(0,-1)
        print(arr)
        ans=[]
        for q in queries :
            l=bisect.bisect_left(arr,q)-1

            r=bisect.bisect_left(arr,q)
            print(l,r)
            k=[]
            if 0<=l<=len(arr)-1 :

                if l+1<len(arr) and arr[l+1]==q :
                    l+=1
                k.append(arr[l])
            else :
                k.append(-1)
            if 0<=r<=len(arr)-1 :
                k.append(arr[r])
            else :
                k.append(-1)
            ans.append(k)
        return ans
        