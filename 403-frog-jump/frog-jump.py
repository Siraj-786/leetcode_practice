class Solution:
    def canCross(self, stones: List[int]) -> bool:
        d=defaultdict(set)
        arr=stones
        s=set(arr)
        if arr[1]!=1 :
            return False 
        d[1].add(1)
        for i in range(1,len(arr)):
            curr=arr[i]
            for ele in d[arr[i]]:
                # print(ele)
                # - 1
                if curr+ele-1>curr :

                    if ele+curr-1 in s :
                        d[ele+curr-1].add(ele-1)

                # equal 
                if ele+curr in s :
                    d[ele+curr].add(ele)
                # + 1
                # print(ele+curr+1)
                if ele+curr+1 in s :
                    # print("ss")
                    d[ele+curr+1].add(ele+1)
        # print(d[arr[-1]])
        # print(d)
        if arr[-1] in d :
            if len(list(d[arr[-1]]))>0 :
                # print(d[arr[-1]])
                return True 

        return False 

        