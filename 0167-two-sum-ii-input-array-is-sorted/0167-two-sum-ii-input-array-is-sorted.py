class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        i=0
        j=len(numbers)-1 
        # k=0
        while i<j :
            now=numbers[i]+numbers[j]
            # print(now)
            if now==target :
                return [i+1,j+1]
            elif now>target :
                j-=1 
            else :
                i+=1 
            # k+=1 
            # if k>10 :
            #     break
            # print(i,j)

            
        