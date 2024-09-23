class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums)<3 :
            return False 

        left=[nums[0]]

        right=nums[1:].copy()
        right.sort()
        for j in range(1,len(nums)-1):
            # print(right)
            ind=bisect.bisect_left(right,nums[j])
            jj=right.pop(ind)
            # print(jj)
            k=bisect.bisect_left(right,jj)
            # if k>len(right)-1 :
            k-=1 
            # print(right,k)
            if left[0]<right[k]<jj :
                return True 
            bisect.insort(left,jj)
            # print("left",left)
        return False 



        