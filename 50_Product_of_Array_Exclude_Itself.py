class Solution:
    """
    @param A: Given an integers array A
    @return: An integer array B and B[i]= A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1]
    """
    def productExcludeItself(self, A):
        # write your code here
        if not A:
            return None
        else:
            B = [1]*len(A)
            for i in range(len(A)):
                for j in range(len(A)):
                    if i != j:
                        B[i] *= A[j]
        return B