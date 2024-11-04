class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        def expand_around_center(left: int, right: int) -> str:
            # Expand the window as long as the characters are the same and within bounds
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return the palindromic substring
            return s[left + 1:right]

        longest_palindrome = ""
        
        for i in range(len(s)):
            # Check for palindrome with a single character center (odd-length)
            palindrome1 = expand_around_center(i, i)
            # Check for palindrome with two consecutive characters center (even-length)
            palindrome2 = expand_around_center(i, i + 1)

            # Update longest palindrome if a longer one is found
            longest_palindrome = max(longest_palindrome, palindrome1, palindrome2, key=len)

        return longest_palindrome
