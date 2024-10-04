class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()  
        n = len(skill)
        target = sum(skill) // (n // 2) 
        total_chemistry = 0

        for i in range(n // 2):
            if skill[i] + skill[n - i - 1] != target:
                return -1  
            total_chemistry += skill[i] * skill[n - i - 1]  

        return total_chemistry
