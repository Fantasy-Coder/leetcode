class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31-1
        #去掉首位一些无关字符
        s = s.strip()
        #如果s为空
        if not s: 
            return 0
        i, sign = 0, 1
        res = 0
        #如果第一个字符是正负号
        if s[0] in '+-':
            sign = 1 if s[0] == '+' else -1
            i += 1
        while i < len(s):
            #如果第i-1个字符不是数字，退出
            if not s[i].isdigit(): 
                break
            #一位一位读取，在第二次循环时往前移，并加上目前正在读取的数字
            res = res * 10 + int(s[i])
            #判断是否溢出，如果溢出，若小于下界则返回下界，反之上界
            if not INT_MIN <= sign * res <= INT_MAX:
                return INT_MIN if sign * res < INT_MIN else INT_MAX
            #继续读取下一个字符
            i += 1
        #返回
        return sign * res