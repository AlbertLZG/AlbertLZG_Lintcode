class Solution:
    # @param k & n  two integer
    # @return ans a integer
    def digitCounts(self, k, n):
        sequence = []
        for i in range(n+1):
            sequence.extend(list(str(i)))
        return sequence.count(str(k))