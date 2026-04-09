class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
      定义dfs函数
        def dfs(grid, i ,j):
            #如果i、j到达边界或者当前位置为0则直接退出
            if not 0 <= i < len(grid) or not 0 <= j < len(grid[0]) or grid[i][j] == '0':
                return
            #当前位置设为0  
            grid[i][j] = '0'
            #递归进行其他位置（实则以上下左右为方向，遍历自身附近所有的位置 若为0则返回 代表着碰到了非陆地）
            dfs(grid, i + 1, j)
            dfs(grid, i, j + 1)
            dfs(grid, i - 1, j)
            dfs(grid, i ,j - 1)
        #初始化count == 0
        count = 0
        #从0，0开始遍历，若某位置为1则代表着有一块陆地，并用dfs函数将附近所有1变成0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(grid, i, j)
                    count += 1
        return count


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #定义bfs
        def bfs(grid, i ,j):
            #建立队列
            queue = [[i, j]]
            #如果队列有元素
            while queue:
                #将队列内第一个元素赋值i，j
                [i, j] = queue.pop(0)
                #如果越界或当前位置为1则置为0
                if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '1':
                    grid[i][j] = '0'
                    #将四个方位全部加入队列
                    queue += [[i + 1, j], [i - 1, j], [i, j - 1], [i, j + 1]]
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '0':
                    continue
                bfs(grid ,i ,j)
                count += 1
                
        return count
