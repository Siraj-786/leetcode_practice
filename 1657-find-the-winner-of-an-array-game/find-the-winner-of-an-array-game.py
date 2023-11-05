class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k>=len(arr) :
            return max(arr)
        c=0
        for i in range(len(arr)):
            if arr[0]<arr[1]:
                c=1  
                p=arr.pop(0)
                arr.append(p)
            else :
                c+=1 
                p=arr.pop(1)
                arr.append(p)
            if c==k :
                return arr[0]
            print(c)
        return arr[0]



        