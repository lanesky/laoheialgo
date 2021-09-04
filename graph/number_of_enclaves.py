# https://leetcode.com/problems/number-of-enclaves/
class Solution(object):
    def numEnclaves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                isBorder = (i == 0 or i == len(grid) -1 or j == 0 or j == len(grid[0]) -1 )
                if not isBorder:
                    continue
                if grid[i][j] != 1:
                    continue
                dfs(i, j, grid)
        
        nums = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    nums += 1
        return nums
                
def dfs(i, j, grid):
    stack = [(i, j)]
    while len(stack) > 0:
        i, j = stack.pop()
        grid[i][j] = 2
        
        neighbours = getNeighbours(i, j, grid)
        for row,col in neighbours:
            if grid[row][col] != 1:
                continue
            stack.append((row, col))
            
def getNeighbours(i, j, grid):
    nodes = []
    #UP
    if i - 1 >= 0:
        nodes.append((i - 1, j))
    #DOWN
    if i + 1 < len(grid):
        nodes.append((i + 1, j))
    #LEFT
    if j - 1 >= 0:
        nodes.append((i, j - 1))
    #RIGHT
    if j + 1 < len(grid[0]):
        nodes.append((i, j + 1))
    return nodes
        
            