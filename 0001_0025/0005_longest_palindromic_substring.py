class Solution:
    def longestPalindrome(self, s: str) -> str:
        #定义一个变量记录最长回文字串
        palindrome = ''
        #从每一个字符出发，分别以该字符为中心（回文长度为奇数）和以该字符与下一个字符之间为中心（回文长度为偶数）进行扩展，找到最长的回文字串
        for i in range(len(s)):
            #以s[i]为中心的回文
            len1 = len(self.getlongestPalindrome(s,i,i))
            if len1 > len(palindrome):
                palindrome = self.getlongestPalindrome(s,i,i)
            #以s[i]和s[i+1]之间为中心的回文
            len2 = len(self.getlongestPalindrome(s,i,i+1))
            if len2 > len(palindrome):
                palindrome = self.getlongestPalindrome(s,i,i+1)
        #返回最长回文字串
        return palindrome
    #定义函数，从中心向两边扩展，找到最长回文字串
    def getlongestPalindrome(self, s , l , r):
        #l和r分别是回文中心的左右指针
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1  
        return s[l+1 : r]




#动态规划
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        
        max_len = 1
        begin = 0
        # dp[i][j] 表示 s[i..j] 是否是回文串
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        
        # 递推开始
        # 先枚举子串长度
        for L in range(2, n + 1):
            # 枚举左边界，左边界的上限设置可以宽松一些
            for i in range(n):
                # 由 L 和 i 可以确定右边界，即 j - i + 1 = L 得
                j = L + i - 1
                # 如果右边界越界，就可以退出当前循环
                if j >= n:
                    break
                    
                if s[i] != s[j]:
                    dp[i][j] = False 
                else:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                
                # 只要 dp[i][L] == true 成立，就表示子串 s[i..L] 是回文，此时记录回文长度和起始位置
                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    begin = i
        return s[begin:begin + max_len]
