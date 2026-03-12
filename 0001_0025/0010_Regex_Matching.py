class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m,n = len(s) + 1,len(p) + 1
        dp = [[False] * n for _ in range(m)]
        dp[0][0] = True
        #初始化首行，s为空字符串，匹配p的情况
        #只有当p的偶数位为*时才能匹配空字符串
        #因为*必须跟在某字符串后面，所以只检查偶数位置，步长2
        for j in range(2,n,2):
            dp[0][j] = dp[0][j - 2] and p[j - 1] =='*'
        #状态转移,遍历s和p所有字符组合，i代表s前i个字符，j代表p前j个字符
        for i in range(1,m):
            for j in range(1,n):
                #如果第j个字符是*号
                if p[j - 1] == '*':
                    #情况1：*匹配前面0个字符 等价于p的前j-2个字符匹配s的前i个字符，忽略第j-1个字符
                    if dp[i][j - 2]:
                        dp[i][j] = True
                    #情况2：*匹配至少1个前面的字符 → 需满足两个条件：
                    # 1. s的前i-1个字符能匹配p的前j个字符（已匹配过）
                    # 2. s的第i个字符和p的第j-1个字符（*前面的字符）相等
                    elif dp[i - 1][j] and s[i - 1] == p[j - 2]:
                        dp[i][j] = True
                    # 情况3：*前面的字符是. , .可以匹配任意字符
                    # 条件：s的前i-1个字符能匹配p的前j个字符
                    elif dp [i - 1][j] and p[j - 2] == '.':
                        dp[i][j] = True
                # 情况2：p的第j个字符不是*
                else:
                    # 情况1：当前字符完全匹配 且 前面的字符也匹配
                    if dp[i - 1][j - 1] and s[i - 1] == p[j - 1]:
                        dp[i][j] = True
                    # 情况2：p的当前字符是.（匹配任意单个字符）且 前面的字符也匹配
                    elif dp[i - 1][j - 1] and p[j - 1] =='.':
                        dp[i][j] = True
        # 返回最终结果：s的全部字符和p的全部字符是否匹配
        return dp[-1][-1]
                    
                


