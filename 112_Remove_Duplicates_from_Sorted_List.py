"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: A ListNode
    @return: A ListNode
    """
    def deleteDuplicates(self, head):
        # write your code here
        elem_now = head
        while elem_now:
            val_now = elem_now.val
            elem_next = elem_now.next
            while elem_next:
                if elem_next.val == val_now:
                    elem_next = elem_next.next
                else:
                    break
            elem_now.next = elem_next
            elem_now = elem_next
        return head