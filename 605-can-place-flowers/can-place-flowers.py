class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # return True if abs(flowerbed.count(0)-flowerbed.count(1))<=1 else False 

        i=0 
        if len(flowerbed)==1 and flowerbed[0]==0 and n==1 :
            return True 
        while i<len(flowerbed):
            if len(flowerbed)>=2 :
                if i==0 :
                    if flowerbed[i]==0 and flowerbed[i+1]==0 :
                        i+=2 
                        n-=1 
                        continue 
                if i==len(flowerbed)-1 and flowerbed[i]==0 and flowerbed[i-1]==0 :
                    i+=2 
                    n-=1 
                    continue 
            if (i-1)>=0 and (i+1)<len(flowerbed) and flowerbed[i-1]==0 and flowerbed[i+1]==0 and flowerbed[i]==0 :
                n-=1
                i+=2
            else : 
                i+=1 
        if n<=0  :
            return True 
        return False 
        