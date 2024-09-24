class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=set()


        def rec(arr,target):
            if sum(arr)==target :
                arr.sort()
                ans.add(tuple(arr))
                return
            elif sum(arr)>target :
                return 
            else :
                for i in range(len(candidates)):
                    arr.append(candidates[i])
                    rec(arr.copy(),target)
                    arr.pop(-1)
            return 
        rec([],target)

        return [list(i) for i in ans]
            

        