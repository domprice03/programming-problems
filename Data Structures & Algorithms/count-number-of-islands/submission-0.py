class Solution:    
    def numIslands(self, grid: List[List[str]]) -> int:
        num = 0
        len_i = len(grid)
        len_j = len(grid[0])

        def dfs(curr: tuple[int, int]) -> None:
            stack: tuple[int, int] = [curr]

            while stack:
                curr = stack.pop(-1)
                i = curr[0]
                j = curr[1]
                grid[i][j] = "0"

                if i > 0 and grid[i-1][j] == "1":
                    curr = (i-1, j)
                    stack.append(curr)
                    grid[curr[0]][curr[1]] == "0"

                if i < len_i - 1 and grid[i+1][j] == "1":
                    curr = (i+1, j)
                    stack.append(curr)
                    grid[curr[0]][curr[1]] == "0"
    
                if j > 0 and grid[i][j-1] == "1":
                    curr = (i, j-1)
                    stack.append(curr)
                    grid[curr[0]][curr[1]] == "0"

                if j < len_j - 1 and grid[i][j+1] == "1":
                    curr = (i, j+1)
                    stack.append(curr)
                    grid[curr[0]][curr[1]] == "0"

        for i in range(len_i):
            for j in range(len_j):
                if grid[i][j] == "1":
                    dfs((i, j))
                    num += 1

        return num
