class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        pre=defaultdict(int)
        for i in range(len(arr)):
            pre[(arr[i]%k+k)%k]+=1 
        for ele in pre :
            if ele!=0 and pre[ele]!=pre[k-ele] :
                # print(ele,pre[ele],pre[k-ele])
                return False 
            if ele==0 and pre[ele]&1 :
                return False 
        return True 
        