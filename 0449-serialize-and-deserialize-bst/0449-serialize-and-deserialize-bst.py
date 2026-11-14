# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        res = []
        def preorder(node):
            if node:
                res.append(str(node.val))
                preorder(node.left)
                preorder(node.right)
        preorder(root)
        return ' '.join(res)
    
    def deserialize(self, data):
        if not data:
            return None
        vals = deque(int(val) for val in data.split(' '))
        def func(minm,maxm):
            if vals and minm < vals[0] < maxm:
                val = vals.popleft()
                node = TreeNode(val)
                node.left = func(minm,node.val)
                node.right = func(node.val,maxm)
                return node
            else:
                return None
        return func(float('-inf'), float('inf'))

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans