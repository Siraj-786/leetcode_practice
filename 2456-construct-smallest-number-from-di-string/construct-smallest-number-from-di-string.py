class Solution:
    def smallestNumber(self, pattern: str) -> str:

        ans=""


        def verify(arr,pattern):
            # print(arr)
            nonlocal ans 
            for i in range(len(pattern)):
                if pattern[i]=="I" :
                    if arr[i]>arr[i+1] :
                        return False 
                else :
                    if arr[i]<arr[i+1] :
                        return False 
            # print("kk")
            if arr :
                ans="".join([str(i) for i in arr])
            return True 


        flag=0



        def generate(s,l):
            nonlocal pattern
            nonlocal flag 
            if flag :
                return 


            if len(s)==l :
                if verify(s,pattern) :
                    flag=1
                    return s
            if len(s)>l :
                return  
            for i in range(1,10):
                if i not in s :
                    s.append(i)
                    generate(s,l)
                    s.pop(-1)
            return -1 

        generate([],len(pattern)+1)
        # print(g)

        return ans 
            



        