class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for ele in asteroids :
            if not stack :
                stack.append(ele)
            elif ele>0 :
                stack.append(ele)
            else :
                stack.append(ele)
                while len(stack)>=2 and stack[-2]>0 and stack[-1]<0 :
                    if abs(stack[-1])>abs(stack[-2]):
                        stack.pop(-2)
                        # break 
                    elif abs(stack[-1])==abs(stack[-2]):
                        stack.pop(-1)
                        stack.pop(-1)
                    else :
                        stack.pop(-1)
                        break 
        return stack 

        return stack 
        