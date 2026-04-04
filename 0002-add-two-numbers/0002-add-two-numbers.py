# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        num1 = ""
        num2 = ""
        curr = l1
        while curr:
            num1 += str(curr.val)
            curr = curr.next
        curr = l2
        while curr:
            num2 += str(curr.val)
            curr = curr.next
        sum = str(int(num1[::-1]) + int(num2[::-1]))[::-1]
        head = None
        curr = None
        for d in sum:
            node = ListNode(int(d))
            if head is None:
                head = node
                curr = node
            else:
                curr.next = node
                curr = node
        return head

        