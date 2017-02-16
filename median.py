# coding:utf-8
'''
@Copyright:LintCode
@Author:   aaajack
@Problem:  http://www.lintcode.com/problem/median
@Language: Python
@Datetime: 17-02-16 13:39
'''

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