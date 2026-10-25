# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        if not root:
            return None

        left = self.flatten(root.left)
        right = self.flatten(root.right)

        if left:
            left.right = root.right
            root.right = root.left
            root.left = None
            
        res = right or left or root
        return res
        


        

        