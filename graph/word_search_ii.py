# https://leetcode.com/problems/word-search-ii/
# Trie + DFS backtracking
# Time O(mn*4^s) | Space O(ws) 
# - where w is the length of list of words,  s is the length of the longest word
class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        trie = {}
        for word in words:
            curr = trie
            for letter in word:
                if letter not in curr:
                    curr[letter] = {}
                curr = curr[letter]
            curr['*'] = word
            
        founds = {}
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in trie:
                    dfs(i, j, board, trie, founds)
        return list(founds.keys())	
  
def dfs(i, j, board, trie, founds):
	if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) :
		return
	curr = board[i][j]
	if curr not in trie:
		return
	trie = trie[curr]
	if "*" in trie:
		founds[trie["*"]] = True
		
	board[i][j] = ""	
	dfs(i, j - 1, board, trie, founds) 
	dfs(i + 1, j, board, trie, founds) 
	dfs(i, j + 1, board, trie, founds) 
	dfs(i - 1, j, board, trie, founds)
	board[i][j] = curr