"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: The first node of linked list.
    @param n: An integer.
    @return: Nth to last node of a singly linked list. 
    """
    def nthToLast(self, head, n):
        # write your code here
        result = head
        if not head:
            return None
            
        for i in range(n-1):
            head = head.next
            if not head:
                return None
        
        while head.next:
            head = head.next
            result = result.next
            
        return result