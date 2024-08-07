class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        for i in range(1,len(numbers)):
            # print(numbers[0:i])
            ind=bisect.bisect_left(numbers[0:i],target-numbers[i])
            # print(ind)
            if target-numbers[i]==numbers[ind] and i!=ind:
                return [ind+1,i+1]

            
        