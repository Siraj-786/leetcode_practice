class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        # Triggered 
        prefix_min_index=[]
        stack=[-1]
        stack_ind=[-1]
        for i in range(len(heights)):
            while stack[-1]>=heights[i] :
                stack.pop(-1)
                stack_ind.pop(-1)
            prefix_min_index.append(stack_ind[-1])
            stack.append(heights[i])
            stack_ind.append(i)
        print(prefix_min_index)



        suffix_min_index=[]
        stack=[-1]
        stack_ind=[len(heights)]
        for i in range(len(heights)-1,-1,-1):
            while stack[0]>=heights[i]:
                stack.pop(0)
                stack_ind.pop(0)
            suffix_min_index.insert(0,stack_ind[0])
            stack.insert(0,heights[i])
            stack_ind.insert(0,i)
        print(suffix_min_index)


        max_area=0
        for i in range(len(heights)):
            max_area=max(max_area,(suffix_min_index[i]-prefix_min_index[i]-1)*heights[i])
        return max_area



        