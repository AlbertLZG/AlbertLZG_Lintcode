# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param l1: the first list
    # @param l2: the second list
    # @return: the sum list of l1 and l2 
    def addLists(self, l1, l2):
        # write your code here
        node = l1
        head = node
        carry = 0
        extra = l2
        while l1.next and l2.next:
            sum = l1.val+l2.val+carry
            node.val = sum%10
            carry = sum/10
            node.next = l1.next
            node = l1.next
            l1 = l1.next
            l2 = l2.next

        sum = l1.val+l2.val+carry
        node.val = sum%10
        carry = sum/10   
        
        if l1.next:
            node.next = l1.next
            node = l1.next
            l1 = l1.next
            while l1.next:
                sum = l1.val+carry
                node.val = sum%10
                carry = sum/10
                node.next = l1.next
                node = l1.next
                l1 = l1.next
            sum = l1.val+carry
            node.val = sum%10
            carry = sum/10
            node.next = l1.next

        if l2.next:
            node.next = l2.next
            node = l2.next
            l2 = l2.next
            while l2.next:
                sum = l2.val+carry
                node.val = sum%10
                carry = sum/10
                node.next = l2.next
                node = l2.next
                l2 = l2.next
            sum = l2.val+carry
            node.val = sum%10
            carry = sum/10
            node.next = l2.next
            
        if carry == 1:
            node.next = extra
            node = node.next
            node.val = carry
            node.next = None            
            
        return head