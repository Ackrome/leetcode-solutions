class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        """
        Calculates the maximum fruits that can be harvested within k steps
        using a sliding window approach.
        """
        left = 0
        max_fruits = 0
        current_fruits = 0

        # The 'right' pointer expands the window.
        for right, (pos_right, amount_right) in enumerate(fruits):
            current_fruits += amount_right

            # The 'left' pointer shrinks the window until the step constraint is met.
            # The condition `left <= right` is the crucial fix to prevent the IndexError.
            while left <= right:
                pos_left = fruits[left][0]

                # Calculate the minimum distance to travel to cover the window [pos_left, pos_right]
                distance = (pos_right - pos_left) + min(abs(startPos - pos_left), abs(startPos - pos_right))

                if distance > k:
                    # If the window is too large, shrink it from the left.
                    current_fruits -= fruits[left][1]
                    left += 1
                else:
                    # The window is valid, no need to shrink further for this 'right' position.
                    break
            
            # Update the maximum fruits found so far with the current valid window.
            max_fruits = max(max_fruits, current_fruits)

        return max_fruits
