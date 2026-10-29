# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next:
            return head
        dummy = ListNode(0, head)
        prev = dummy
    
        while prev.next:
            if not prev.next.next:
                break

            first = prev.next
            second = first.next

            prev.next = second
            first.next = second.next
            second.next = first
            
            prev = first
        return dummy.next
