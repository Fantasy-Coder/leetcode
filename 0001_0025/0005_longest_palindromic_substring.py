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
