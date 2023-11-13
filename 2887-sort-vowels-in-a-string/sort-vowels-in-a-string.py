from collections import defaultdict
class Solution:
    def sortVowels(self, s: str) -> str:
        d = defaultdict(int)
        d["A"] = 0
        d["E"] = 0
        d["I"] = 0
        d["O"] = 0
        d["U"] = 0
        d["a"] = 0
        d["e"] = 0
        d["i"] = 0
        d["o"] = 0
        d["u"] = 0
        for i in s:
            if i in d:
                d[i] += 1
        print(d)
        vowels =["A","E","I","O","U","a","e","i","o","u"]
        counts=[d[i] for i in vowels]
        ans=""
        for i in s :
            if i not in vowels:
                ans+=i
            else:
                for c in range(len(counts)) :
                    if counts[c]>0 :
                        ans+=vowels[c]
                        counts[c]-=1
                        break
                        
                        
        return ans
