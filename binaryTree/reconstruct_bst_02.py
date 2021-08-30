
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
        config = [0]
        bst = buildTree(float('-inf'), float('inf'), preorder, config)
        return bst
    
#Time O(n) | Space O(d)       
def buildTree(lo, hi, preorder, config):
    gidx = config[0]
    if gidx == len(preorder):
        return None
    
    value = preorder[gidx]
    if value < lo or value > hi:
        return None
    
    config[0] += 1
    l = buildTree(lo, value, preorder, config)
    r = buildTree(value, hi, preorder, config)
    
    return TreeNode(value, l, r)