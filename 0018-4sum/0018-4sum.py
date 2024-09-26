class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums.sort()

        ans=set()

        if len(nums)<=3 :
            return []
        for i in range(len(nums)-3):
            for j in range(i+1,len(nums)-2) :
                a,b=nums[i],nums[j]
                x=j+1
                y=len(nums)-1
                if a+b+nums[x]+nums[y]==target :
                    ans.add(tuple([a,b,nums[x],nums[y]]))
                while x<y :
                    if a+b+nums[x]+nums[y]<=target :
                        x+=1 
                    else :
                        y-=1 
                    if a+b+nums[x]+nums[y]==target and x!=y:
                        ans.add(tuple([a,b,nums[x],nums[y]]))
        return [list(i) for i in ans]
                    

        