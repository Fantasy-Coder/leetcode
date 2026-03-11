class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x< 10:
            return True
        digits = []
        temp = x
        while temp > 0:
            digits.append(temp%10)
            temp = temp//10
        for a in range(len(digits)//2):
            if digits[a] != digits[len(digits)- a - 1]:
                return False
        return True