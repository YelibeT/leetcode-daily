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
        def recurse(curr1, curr2, curr3, carry):
            if not curr1 and not curr2:
                if carry != 0:
                    curr3.next = ListNode(carry)
                return 
            if curr1 and not curr2:
                ans = curr1.val + carry
                curr1 = curr1.next
            elif curr2 and not curr1:
                ans = curr2.val + carry
                curr2 = curr2.next
            else:
                ans = curr1.val + curr2.val + carry
                curr1 = curr1.next
                curr2 = curr2.next
            if ans >= 10:
                ans %= 10
                carry = 1
            else:
                carry = 0
            curr3.next = ListNode(ans)
            return recurse(curr1, curr2, curr3.next, carry)
        recurse(curr1, curr2, curr3, 0)
        return res.next