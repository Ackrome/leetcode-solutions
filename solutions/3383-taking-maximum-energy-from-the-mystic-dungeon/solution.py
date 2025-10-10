class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        lastK = energy[-k:][::-1]
        for i in range(len(energy) - k - 1, -1, -1):
            lastK.append(lastK[-k] + energy[i])
        return max(lastK)
