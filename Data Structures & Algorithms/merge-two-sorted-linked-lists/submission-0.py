# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        f1, f2 = list1, list2
        last = ListNode()
        start = last
        while f1 and f2:
            if f1.val <= f2.val:
                last.next = f1
                f1 = f1.next
            else:
                last.next = f2
                f2 = f2.next
            last = last.next

        if f1:
            last.next = f1
        elif f2:
            last.next = f2

        return start.next