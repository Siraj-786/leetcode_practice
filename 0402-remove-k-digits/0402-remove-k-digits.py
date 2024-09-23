class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num)==1 and k>=1:
            return "0"

        stack=[]
        for i in range(len(num)):
            
            while stack and stack[-1]>num[i] and k>0 :
                stack.pop(-1)
                k-=1
            stack.append(num[i])
        
        while stack and stack[0]=="0" :
            stack.pop(0)
        while k and stack  :
            stack.pop(-1)
            k-=1 
        # print(stack)
        if not stack :
            return "0"
        return "".join(stack) 

        