# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        def helper(node, val):
            if not node:
                return None
            if val < node.val:
                node = self.searchBST(node.left, val)
            elif val > root.val:
                node = self.searchBST(node.right, val)
            else:
                return node
            return node 
        return helper(root,val)