# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """

        left child pointer is null
        order -> as the pre-order traversal of the binary tree

        """
        def recurse(root):
            if not root:
                return None
            left = recurse(root.left) 
            right = recurse(root.right)
            #edge case: if one of em is empty
            if left:#it should have no left child
                left.right = root.right
                root.right = root.left
                root.left = None
            res = right or left or root #the order matters
            return res
        return recurse(root)




        

        