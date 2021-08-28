# https://leetcode.com/problems/binary-tree-maximum-path-sum/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    # Time O(n) | Space O(log(n))
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        maxValues = [float('-inf')]
        findSumPathAsBranch(root, maxValues)
        return maxValues[0]
    
def findSumPathAsBranch(node, maxValues):
    if node is None:
        return 0
    
    l = findSumPathAsBranch(node.left, maxValues)
    r = findSumPathAsBranch(node.right, maxValues)
    value = node.val
    
    maxValues[0] = max(maxValues[0], l + r + value)
    
    return max(0, max(l, r) + value)
    