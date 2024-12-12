class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts.sort()
        p1=0 
        while p1<k :
            p=gifts.pop(-1)
            p=math.floor(math.sqrt(p))
            bisect.insort(gifts,p)
            p1+=1 
        return sum(gifts)
        