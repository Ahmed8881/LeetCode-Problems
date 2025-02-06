class Solution(object):
    def postorderTraversal(self, root):
        def helper(node, tree):
            if node is None:
                return
            helper(node.left, tree)
            helper(node.right, tree)
            tree.append(node.val)

        tree = []
        helper(root, tree)
        return tree
