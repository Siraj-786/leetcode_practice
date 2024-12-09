class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        pre=-1 
        prev=[]
        for i in range(len(nums)):
            if i==0 :
                prev.append(pre)
            else :
                if nums[i]&1 == nums[i-1]&1 :
                    pre=i-1
                prev.append(pre)
        print(prev)
        ans=[]
        for q in queries :
            a,b=q[0],q[1]
            limit=prev[b]
            if limit<a :
                ans.append(True)
            else :
                ans.append(False)
        return ans 

        