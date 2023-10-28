class Solution:
    def countVowelPermutation(self, n: int) -> int:
        # a==0 ,e==1, i==2 ,o===3 ,u===4

        #a:[e]
        #e:[a,i]
        #i:[a,e,o,u]
        #o:[i,u]
        #u:[a]


        # converting everything with index perspective so as to easy access

    
        d={0:[1],1:[0,2],2:[0,1,3,4],3:[2,4],4:[0]}
        arr=[1,1,1,1,1]
        mod=(10**9)+7
        for i in range(n-1):
            new_arr=[0,0,0,0,0]
            for ind in range(5):
                for ele in d[ind]:
                    new_arr[ele]=(new_arr[ele]%mod+arr[ind]%mod)%mod
            arr=new_arr
        return sum(arr)%mod