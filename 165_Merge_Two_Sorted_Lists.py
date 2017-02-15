"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param two ListNodes
    @return a ListNode
    """
    def mergeTwoLists(self, l1, l2):
        # write your code here
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val<l2.val:
            head, l1_ind, l2_ind = l1, l1.next, l2 
        else:
            head, l1_ind, l2_ind = l2, l1, l2.next
        result = head
        while l1_ind and l2_ind:
            if l1_ind.val < l2_ind.val:
                head.next = l1_ind
                head = head.next
                l1_ind = l1_ind.next
            else:
                head.next = l2_ind
                head = head.next
                l2_ind = l2_ind.next
        if l1_ind:
            head.next = l1_ind
        if l2_ind:
            head.next = l2_ind
        
        return result