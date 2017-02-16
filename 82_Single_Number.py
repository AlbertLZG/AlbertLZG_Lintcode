class Solution:
    """
    @param A : an integer array
    @return : a integer
    """
    def singleNumber(self, A):
        # write your code here
        if not A:
            return 0
        else:
            B = []
            for i in range(len(A)):
                if A[i] in B:
                    B.remove(A[i])
                else:
                    B.append(A[i])
        return B[0]
            