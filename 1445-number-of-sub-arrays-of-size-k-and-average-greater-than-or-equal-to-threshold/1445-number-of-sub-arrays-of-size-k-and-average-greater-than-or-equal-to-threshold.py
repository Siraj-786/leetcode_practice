class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        

        c=0
        q=[]
        s=0
        for i in range(len(arr)):
            if len(q)<k :
                q.append(arr[i])
                s+=arr[i]
            if len(q)==k :
                suumm=s/k 
                if suumm>=threshold :
                    c+=1 
                s-=q[0]
                q.pop(0)
        return c 
