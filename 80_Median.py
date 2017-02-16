class Solution:
    """
    @param nums: A list of integers.
    @return: An integer denotes the middle number of the array.
    """
    def median(self, nums):
        # write your code here
        if not nums:
            return None
        else:
            nums.sort()
            return nums[(len(nums)-1)/2]