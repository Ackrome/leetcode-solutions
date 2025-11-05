from sortedcontainers import SortedList
from collections import defaultdict
from typing import List

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        res = []  # This will store the results of top x sums for each window
        top = SortedList()  # Sorted list to store the top x frequent elements
        low = SortedList()  # Sorted list to store other candidate frequent elements
        curr = 0  # This is the sum of the top x frequent elements in the current window
        fm = defaultdict(int)  # Frequency map to store the counts of elements

        # Helper function to update frequencies and adjust top x elements
        def change(num, count):
            nonlocal curr
            prev = (fm[num], num)
            if fm[num]:
                # Remove the element from low or top based on its previous frequency
                if prev in low:
                    low.discard(prev)
                else:
                    top.discard(prev)
                    curr -= fm[num] * num  # Remove the previous contribution to sum

            fm[num] += count  # Update frequency of the element
            if fm[num]:
                low.add((fm[num], num))  # Add to low if frequency > 0

            # Move elements from low to top until top contains x elements
            while low and len(top) < x:
                freq, key = low.pop(-1)
                curr += freq * key  # Add to the current sum
                top.add((freq, key))

            # Balance between low and top to make sure top always has the most frequent elements
            while low and low[-1] > top[0]:
                freq, key = low.pop(-1)
                xfreq, xkey = top.pop(0)
                curr = curr - xfreq * xkey + freq * key  # Update sum
                low.add((xfreq, xkey))
                top.add((freq, key))

        # Sliding window: iterate through the array and maintain the frequency counts
        for i in range(n):
            change(nums[i], 1)  # Add current element to the window
            if i >= k: change(nums[i-k], -1)  # Remove element that is no longer in the window
            if i >= k - 1: res.append(curr)  # After the window is fully formed, add the current sum

        return res
