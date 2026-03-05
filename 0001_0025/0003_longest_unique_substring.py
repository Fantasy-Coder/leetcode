class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
       ans = left = 0
       window = {}
       for right, c in enumerate(s):
           if c in window:
               left = max(window[c] + 1, left)
           window[c] = right
           ans = max(ans, right - left + 1)
       return ans            