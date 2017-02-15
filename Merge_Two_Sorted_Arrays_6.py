class Solution:
    #@param A and B: sorted integer array A and B.
    #@return: A new sorted integer array
    def mergeSortedArray(self, A, B):
        # write your code here
        res = []
        indexA = indexB = 0
        for i in range(len(A)+len(B)):
            if A[indexA]<B[indexB]:
                res.append(A[indexA])
                indexA += 1
            else:
                res.append(B[indexB])
                indexB += 1
            if indexA == len(A):
                res.extend(B[indexB:])
                break
            elif indexB == len(B):
                res.extend(A[indexA:])
                break
            else:
                pass
        return res