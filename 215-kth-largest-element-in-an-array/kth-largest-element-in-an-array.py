import heapq
print(dir(heapq)) 
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # heapq.heapify(nums)
        # for i in range(len(nums)-k):
        #     heapq.heappop(nums)
        # return nums[0]

        nums=[-i for i in nums]
        heapq.heapify(nums)
        for i in range(k-1):
            heapq.heappop(nums)
        return -nums[0]


        
        