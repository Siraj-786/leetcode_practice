class Solution:
    def numTeams(self, rating: List[int]) -> int:

        l1=[rating[0]]
        pre_maxis=[0]
        pre_minis=[0]
        for i in range(1,len(rating)):
            ind=bisect.bisect(l1,rating[i])
            pre_maxis.append(len(l1)-ind)
            pre_minis.append(ind)
            bisect.insort(l1,rating[i])
        print(pre_maxis)
        print(pre_minis)
        # return 3 
        l1=[rating[-1]] 
        suf_maxis=[0]
        suf_minis=[0]
        for i in range(len(rating)-2,-1,-1):
            ind=bisect.bisect(l1,rating[i])
            suf_maxis.insert(0,len(l1)-ind)
            suf_minis.insert(0,ind)
            bisect.insort(l1,rating[i])
        print(suf_maxis)
        print(suf_minis)
        ans=0

        for i in range(len(pre_maxis)):
            ans+=pre_maxis[i]*suf_minis[i]
            ans+=pre_minis[i]*suf_maxis[i]
        return ans


        

        