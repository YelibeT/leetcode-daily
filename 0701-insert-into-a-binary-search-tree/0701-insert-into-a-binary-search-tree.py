# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        if not root:
            root = TreeNode(val)
            return root
        def helper(node, val):
            if not node:
                return None
            if val > node.val:
                if not node.right:
                    node.right = TreeNode(val)
                    return
                helper(node.right, val)
            else:
                if not node.left:
                    node.left = TreeNode(val)
                    return 
                helper(node.left, val)
        helper(root, val)
        return root