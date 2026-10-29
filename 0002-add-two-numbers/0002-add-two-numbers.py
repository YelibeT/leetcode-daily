# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        curr1 = l1
        curr2 = l2
        carry = 0
        res = ListNode()
        curr3 = res
        while curr1 and curr2:
            ans = curr1.val + curr2.val + carry
            if ans >= 10:
                ans %= 10
                carry = 1
            else: 
                carry = 0
            curr1 = curr1.next
            curr2 = curr2.next
            curr3.next = ListNode(ans)
            curr3 = curr3.next
        while curr1:
            ans = curr1.val + carry
            if ans >= 10:
                ans %= 10
                carry = 1
            else: 
                carry = 0
            curr3.next = ListNode(ans)
            curr3 = curr3.next
            curr1 = curr1.next
        while curr2:
            ans = curr2.val + carry
            if ans >= 10:
                ans %= 10
                carry = 1
            else: 
                carry = 0
            curr3.next = ListNode(ans)
            curr3 = curr3.next
            curr2 = curr2.next
        if carry == 1:
            curr3.next = ListNode(carry)
        return res.next
            