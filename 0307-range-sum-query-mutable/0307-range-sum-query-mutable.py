class NumArray:

    # Segment tree node
    class Node:
        def __init__(self):
            self.sum = 0
            self.left = None
            self.right = None

    def __init__(self, nums):
        self.n = len(nums)
        self.root = self.buildST(nums, 0, self.n - 1) if self.n > 0 else None

    def buildST(self, nums, s, e):
        node = self.Node()

        # Leaf node
        if s == e:
            node.sum = nums[s]
            return node

        mid = s + (e - s) // 2

        node.left = self.buildST(nums, s, mid)
        node.right = self.buildST(nums, mid + 1, e)

        node.sum = node.left.sum + node.right.sum
        return node

    def update(self, index, val):
        self.updateUtil(index, val, 0, self.n - 1, self.root)

    def updateUtil(self, index, val, s, e, node):
        # Reach the target leaf
        if s == e:
            node.sum = val
            return

        mid = s + (e - s) // 2

        if index <= mid:
            self.updateUtil(index, val, s, mid, node.left)
        else:
            self.updateUtil(index, val, mid + 1, e, node.right)

        # Recalculate the current segment sum
        node.sum = node.left.sum + node.right.sum

    def sumRange(self, left, right):
        return self.sumUtil(left, right, 0, self.n - 1, self.root)

    def sumUtil(self, qs, qe, s, e, node):
        # No overlap
        if e < qs or s > qe:
            return 0

        # Complete overlap
        if qs <= s and e <= qe:
            return node.sum

        # Partial overlap
        mid = s + (e - s) // 2

        leftSum = self.sumUtil(qs, qe, s, mid, node.left)
        rightSum = self.sumUtil(qs, qe, mid + 1, e, node.right)

        return leftSum + rightSum