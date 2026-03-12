class Solution:
    def isPalindrome(self, x: int) -> bool:
        #负数不是回文数
        if x < 0:
            return False
        #正的个位数是回文数
        if x< 10:
            return True
        #将数字的每一位存入列表中，判断列表前后是否相等
        digits = []
        temp = x
        #将数字的每一位存入列表中
        while temp > 0:
            digits.append(temp%10)
            temp = temp//10
        #判断列表前后是否相等
        for a in range(len(digits)//2):
            if digits[a] != digits[len(digits)- a - 1]:
                return False
        return True