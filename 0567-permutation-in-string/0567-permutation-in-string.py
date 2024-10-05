class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dic1={}
        for ele in s1 :
            if ele in dic1 :
                dic1[ele]+=1
            else :
                dic1[ele]=1
        dic2={}
        for ele in s2[0:len(s1)] :
            if ele in dic2 :
                dic2[ele]+=1
            else :
                dic2[ele]=1
        if dic1==dic2 :
            return True
        for i in range(1,len(s2)-len(s1)+1):
            if dic2[s2[i-1]]==1 :
                del dic2[s2[i-1]]
            else :
                dic2[s2[i-1]]-=1
            if s2[i-1+len(s1)] in dic2 :
                dic2[s2[i-1+len(s1)]]+=1
            else :
                dic2[s2[i-1+len(s1)]]=1
            if dic1==dic2 :
                return True
        return False

            
            
        return False
        