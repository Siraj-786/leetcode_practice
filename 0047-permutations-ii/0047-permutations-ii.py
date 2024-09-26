class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans=set()

        def rec(arr,index_arr):
            if len(arr)==len(nums):
                ans.add(tuple(arr))
            if len(arr)>=9 :
                return 

            for i in range(len(index_arr)):
                if index_arr[i]==0 :
                    index_arr[i]=1
                    rec(arr+[nums[i]],index_arr)
                    index_arr[i]=0
        rec([],[0]*len(nums))
        return [list(i) for i in ans]


        