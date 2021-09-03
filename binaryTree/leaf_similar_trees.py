https://leetcode.com/problems/leaf-similar-trees/

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, val=0, left=None, right=None):
    #         self.val = val
    #         self.left = left
    #         self.right = right

class Solution(object):
# ===== SOLUTION 1 ======
#     # Time O(n + m) | Space (Leaf1 + Leaf2) 
#     def leafSimilar(self, root1, root2):
#         leaves1 = []
#         leaves2 = []
        
#         traverse(root1, leaves1)
#         traverse(root2, leaves2)
        
#         return leaves1 == leaves2
    
# def traverse(node, leaves):
#     if node.left is None and node.right is None:
#         leaves.append(node.val)
#         return
#     if node.left is not None:
#         traverse(node.left, leaves)
#     if node.right is not None:
#         traverse(node.right, leaves)

# ===== SOLUTION 2 ======
    # Time O(n + m) | Space O(h1 + h2) 
    def leafSimilar(self, root1, root2):
        stack1 = [ root1 ]
        stack2 = [ root2 ]
        while len(stack1) > 0 and len(stack2) > 0:
            leaf1 = getNextLeafNode(stack1)
            leaf2 = getNextLeafNode(stack2)
            if leaf1.val != leaf2.val:
                return False
        return len(stack1) == 0 == len(stack2)
    
def getNextLeafNode(stack):
    while len(stack) > 0:
        curr = stack.pop()
        if curr.left is None and curr.right is None:
            return curr
        if curr.left is not None:
            stack.append(curr.left)
        if curr.right is not None:
            stack.append(curr.right)    
