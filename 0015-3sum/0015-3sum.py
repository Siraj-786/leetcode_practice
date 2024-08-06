class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if nums.count(0)==len(nums):
            return [[0,0,0]]
        nums.sort()
        ans=set()
        for i in range(1,len(nums)-1):
            p=i-1
            s=i+1 
            while p>=0 and s<=len(nums)-1 :
                if nums[p]+nums[i]+nums[s]==0 :
                    ans.add((nums[p],nums[i],nums[s]))
                    # ans+=1 
                    if p>=1 :
                        p-=1 
                        while p>=1 :
                            if nums[p]==nums[p-1]:
                                p-=1 
                            else :
                                break 
                    else :
                        s+=1 
                        while s<len(nums)-2 :
                            if nums[s]==nums[s+1]:
                                s+=1
                            else :
                                break 
                else :
                    if nums[p]+nums[i]+nums[s]>0 :
                        p-=1 
                    else :
                        s+=1 
        # print(ans)
        new_ans=[]
        for ele in ans :
            new_ans.append(list(ele))
        return new_ans




        