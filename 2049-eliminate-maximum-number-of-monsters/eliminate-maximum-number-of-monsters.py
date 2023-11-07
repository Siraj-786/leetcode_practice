class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        arrival = [dist[i] / speed[i] for i in range(len(speed))]
        arrival.sort()
        ans = 0

        for i in range(len(arrival)):
            if arrival[i] <= i:
                break
                
            ans += 1

        return ans