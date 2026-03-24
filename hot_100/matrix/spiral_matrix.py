from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        #左、右、上、下边界的初始值以及返回的结果列表
        l, r, t, b, res =0, len(matrix[0]) - 1, 0, len(matrix) -1, [] 
        #循环
        while True:
            #从左到右遍历，将数字写入
            for i in range(l, r + 1):
                res.append(matrix[t][i])
            #上边界下移    
            t += 1
            #如果上边界在下边界的下面则返回
            if t > b:
                break
            #从上到下遍历    
            for i in range(t , b + 1):
                res.append(matrix[i][r])
            r -= 1
            if l > r:
                break
            #从右到左遍历
            for i in range(r , l - 1, -1):
                res.append(matrix[b][i])
            b -= 1
            if t > b:
                break
            #从下到上遍历    
            for i in range(b , t - 1, -1):
                res.append(matrix[i][l])
            l += 1
            if l > r:
                break
        return res