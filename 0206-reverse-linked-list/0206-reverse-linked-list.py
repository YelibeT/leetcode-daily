# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr = head
        prev = None
        def recurse(curr, prev):
            if not curr:
                return prev
            saved = curr.next
            curr.next = prev
            return recurse(saved, curr)
        return recurse(curr, prev)
            
        