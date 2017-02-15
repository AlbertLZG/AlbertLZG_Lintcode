class Solution:
    """
    @param {int} n an integer.
    @return {int} the nth prime number as description.
    """
    def nthUglyNumber(self, n):
        # write your code here
        ugly = [1]
        index2 = 0
        index3 = 0
        index5 = 0
        for i in range(n):
            temp_ugly = min(ugly[index2]*2,ugly[index3]*3,ugly[index5]*5)
            ugly.append(temp_ugly)
            index2 +=1 if temp_ugly >= ugly[index2]*2 else 0
            index3 +=1 if temp_ugly >= ugly[index3]*3 else 0
            index5 +=1 if temp_ugly >= ugly[index5]*5 else 0
        return ugly[n-1]