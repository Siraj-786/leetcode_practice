class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        i=0
        s=nums[0:k]
        s.sort()
        ans=[s[-1]]
        for j in range(k,len(nums)):
            # print(s)
            f=bisect.bisect_left(s,nums[i])
            s.pop(f)
            insort(s,nums[j])
            ans.append(s[-1])
            i+=1
        return ans

        