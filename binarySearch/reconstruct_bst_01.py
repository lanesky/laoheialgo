# https://leetcode.com/problems/binary-tree-maximum-path-sum/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        bst = buildTree(preorder)
        return bst
# Time O(n^2) | Space O(d)    
def buildTree(preorder):
    if len(preorder) == 0:
        return None
    
    rootValue = preorder[0]
    ridx = len(preorder)
    for i in range(1, len(preorder)):
        if preorder[i] > rootValue:
            ridx = i
            break
    l = buildTree(preorder[1:ridx])
    r = buildTree(preorder[ridx:])
    
    return TreeNode(rootValue, l, r)