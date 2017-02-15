class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be inserted
    @return : an integer
    """
    def searchInsert(self, A, target):
        # write your code here
        if not A:
            return 0
        else:
            head = 0
            tail = len(A)-1
            while head < tail-1:
                mid = (head+tail)/2
                if A[mid] > target:
                    tail = mid
                else:
                    head = mid
            if A[head] == target or A[head] > target:
                return head
            elif A[tail] == target or (A[head] < target and A[tail] > target):
                return tail
            elif A[tail] < target:
                return tail+1
            