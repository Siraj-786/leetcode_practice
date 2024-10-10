class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        indices = [i for i in range(n)]

        # Sort indices based on corresponding values in nums and ensure stability
        indices.sort(key=lambda i: (nums[i], i))

        min_index = indices[0]  # Minimum index encountered so far
        max_width = 0
        print(indices)

        # Calculate maximum width ramp
        for i in indices:
            max_width = max(max_width, i - min_index)
            min_index = min(min_index, i)
            print(i,min_index)

        return max_width