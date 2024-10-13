class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        num=[]

        k=1
        for ele in nums:
            for c in ele :
                num.append((c,k))
            k+=1 
        num.sort()
        d=defaultdict(int)
        min_len=float("inf")
        l,r=float("-inf"),float("inf")
        q=[]
        for ele in num :
            d[ele[1]]+=1
            q.append(ele)
            if len(d)==len(nums):
                t=q[-1][0]-q[0][0]
                if t<min_len :
                    min_len=t 
                    l=q[0][0]
                    r=q[-1][0]
                while len(d)==len(nums) :
                    p=q.pop(0)
                    d[p[1]]-=1
                    if d[p[1]]==0 :
                        del d[p[1]]
                    if len(d)==len(nums) :
                        t=q[-1][0]-q[0][0]
                        if t<min_len :
                            min_len=t 
                            l=q[0][0]
                            r=q[-1][0]
        return [l,r]







        
        