class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)
        def check (min_power, add_station):
            window = sum(stations[:r])
            add = [0] * n
            for i in range(n):
                if i + r < n:
                    window += stations[i + r]
                if i > r:
                    window -= stations[i - r - 1] + add[i - r - 1]
                if window < min_power:
                    need = min_power - window
                    if need > add_station:
                        return False
                    add[min(n - 1, i + r)] += need
                    window = min_power
                    add_station -= need
            return True
        low = 0
        high = sum(stations) + k
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            if check(mid, k):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans
