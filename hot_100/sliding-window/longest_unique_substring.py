class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
       #ans记录最长长度，left记录窗口左边界，window记录窗口内字符最后出现的位置
       ans = left = 0
       window = {}
       #right遍历字符串，c为当前字符
       for right, c in enumerate(s):
            #如果c在窗口内，则更新左边界
           if c in window:
               #更新左边界为c上次出现位置的下一位和当前左边界的较大值，保证左边界不会回退
               left = max(window[c] + 1, left)
           #更新c在窗口内最后出现的位置
           window[c] = right
           #更新最长长度
           ans = max(ans, right - left + 1)
       #返回最长长度
       return ans            