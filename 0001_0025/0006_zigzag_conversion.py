class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # 特殊情况：行数为1或行数大于等于字符串长度，直接返回原字符串
        if numRows == 1 or numRows >= len(s):
            return s
        
        # 初始化每行的字符串列表
        rows = [''] * numRows
        current_row = 0  # 当前所在行
        direction = -1   # 移动方向：-1表示向上，1表示向下
        
        for char in s:
            # 将当前字符添加到对应行
            rows[current_row] += char
            
            # 到达第一行或最后一行时，改变移动方向
            if current_row == 0 or current_row == numRows - 1:
                direction *= -1
            
            # 移动到下一行
            current_row += direction
        
        # 将所有行的字符串拼接起来
        return ''.join(rows)