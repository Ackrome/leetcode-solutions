class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Case 1: The array already contains at least one '1'.
        # Each '1' can be used to convert its neighbors. The minimum operations
        # needed is simply the number of elements that are not '1'.
        ones = nums.count(1)
        if ones > 0:
            return n - ones

        # Case 2: The array contains no '1's.
        # We must first create a '1' by finding the shortest subarray with a GCD of 1.
        min_len = float('inf')

        for i in range(n):
            current_gcd = nums[i]
            for j in range(i + 1, n):
                current_gcd = math.gcd(current_gcd, nums[j])
                if current_gcd == 1:
                    # Found a subarray nums[i...j] with GCD of 1.
                    # The length is j - i + 1.
                    min_len = min(min_len, j - i + 1)
                    break  # Optimization: move to the next starting element i
        
        # Case 3: Impossible to create a '1'.
        # If min_len was not updated, it means no subarray has a GCD of 1.
        # This also implies the GCD of the entire array is > 1.
        if min_len == float('inf'):
            return -1

        # The number of operations is (min_len - 1) to create the first '1',
        # plus (n - 1) operations to propagate that '1' to all other elements.
        return (min_len - 1) + (n - 1)
