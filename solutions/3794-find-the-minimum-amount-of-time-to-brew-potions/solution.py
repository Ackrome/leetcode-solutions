class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n, m = len(skill), len(mana)
        prefix_skills = [0] * n
        for i in range(1, n):
            prefix_skills[i] = prefix_skills[i - 1] + skill[i]

        total_time = skill[0] * mana[0]

        for j in range(1, m):
            max_time = skill[0] * mana[j]
            for i in range(1, n):
                diff_time = prefix_skills[i] * mana[j - 1] - prefix_skills[i - 1] * mana[j]
                if diff_time > max_time:
                    max_time = diff_time
            total_time += max_time

        return total_time + prefix_skills[-1] * mana[-1]
