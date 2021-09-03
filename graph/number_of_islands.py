# https://leetcode.com/problems/number-of-islands/

class Solution(object):
    
    #Time O(m*n) | Space O(m*n)
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        islands = 0
        visited = [[False for _ in row] for row in grid]
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if visited[i][j]:
                    continue
                if grid[i][j] == "1":
                    islands += 1
                    dfs(i, j, grid, visited)
        return islands
    
def dfs(row, col, grid, visited):
    stack = [(row, col)]
    while len(stack) > 0:
        i, j = stack.pop()
        visited[i][j] = True
        if grid[i][j] == "0":
            continue
        nodes = getUnvisitedNeighbours(i, j, grid, visited)
        for node in nodes:
            stack.append(node)

def getUnvisitedNeighbours(i, j, grid, visited):
    nodes = []
    
    #UP
    if i - 1 >= 0 and not visited[i - 1][j]:
        nodes.append((i - 1, j))
    #DOWN
    if i + 1 < len(grid) and not visited[i + 1][j]:
        nodes.append((i + 1, j))
    #LEFT
    if j - 1 >= 0 and not visited[i][j - 1]:
        nodes.append((i, j - 1))
    #RIGHT
    if j + 1 < len(grid[0]) and not visited[i][j + 1]:
        nodes.append((i, j + 1))
    
    return nodes
