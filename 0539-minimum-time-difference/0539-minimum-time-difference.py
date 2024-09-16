class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:

        new=[]
        for i in range(len(timePoints)):
            k= [p for p in timePoints[i].split(":")]
            h=int(k[0])
            m=int(k[1])
            new.append(h*60+m)
        print(new)
        new.sort()
        mini=float("inf")
        for i in range(len(new)-1):
            if i==0 :
                mini=min(mini,new[i+1]-new[i])  # right 
                mini=min(mini,new[i]+60*24-new[-1])
            else :
                mini=min(mini,new[i+1]-new[i],new[i]-new[i-1])
        return mini




        