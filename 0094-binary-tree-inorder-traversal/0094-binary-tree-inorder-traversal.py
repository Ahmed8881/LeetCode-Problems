# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        def helper(node, tree):
            if node is None:
                return
            helper(node.left, tree)   
            tree.append(node.val)     
            helper(node.right, tree) 

        tree = []
        helper(root, tree)
        return tree
 
        