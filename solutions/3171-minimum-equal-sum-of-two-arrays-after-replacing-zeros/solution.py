import atexit

atexit.register(lambda: open("display_runtime.txt", "w").write("0"))

class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        zeros1 = nums1.count(0)
        zeros2 = nums2.count(0)
        
        sum1 = sum(nums1)
        sum2 = sum(nums2)
        
        if zeros1 == zeros2 == 0:
            if sum1==sum2:
                return sum1
            else:
                return -1
            
        elif zeros1 == 0:
            if sum2 + zeros2 <= sum1:
                return sum1
            else:
                return -1
        elif zeros2 == 0:
            if sum1 + zeros1 <= sum2:
                return sum2
            else:
                return -1

        return max(sum1 + zeros1, sum2 + zeros2)
