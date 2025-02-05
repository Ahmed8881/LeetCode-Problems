# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        current=head
        while current and current.next:
            if current.val==current.next.val:
                current.next=current.next.next
            else:
                current=current.next
        return head

        