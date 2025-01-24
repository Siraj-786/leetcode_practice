class Solution:
    def reverseVowels(self, s: str) -> str:
        l=['a',"e","i", "o","u", "A","E",'I','O','U']
        v=[]
        non=[]
        for ele in s :
            if ele in l :
                v.append(ele) 
            else :
                non.append(ele)
        v=v[::-1]
        ans=[]
        for ele in s :
            if ele in l :
                ans.append(v.pop(0))
            else :
                ans.append(ele)
        return "".join(ans )
                
        