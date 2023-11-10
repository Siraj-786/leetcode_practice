from typing import List
from collections import defaultdict
class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        count_hash = defaultdict(int)  # for finding that occurs only once
        for i in (adjacentPairs):
            count_hash[i[0]] += 1
            count_hash[i[1]] += 1
            
            
            
        connection = defaultdict(list)   # stores the connection between nodes [l,r] of [r,l]  anything is possible 
        for i in (adjacentPairs):
            connection[i[0]].append(i[1])
            connection[i[1]].append(i[0])
            
            
        head = -1
        for k in count_hash:
            if count_hash[k] == 1:
                head= k
                break
                
        
        l1 = [head]
        s=set()
        s.add(head)
        for i in range(len(adjacentPairs)):
            for ele in connection[head]:
                if ele not in s:
                    s.add(ele)
                    l1.append(ele)
                    head = ele
                    break
                    
            
            
            
        return l1



