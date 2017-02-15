class Solution:
    # @param nums: The integer array
    # @param target: Target number to find
    # @return the first position of target in nums, position start from 0 
    def binarySearch(self, nums, target):
        # write your code here
        ind_left = 0 
        ind_right = len(nums)-1
        while ind_left < ind_right:
            if ind_left == ind_right-1:
                if nums[ind_left] == target:
                    return ind_left
                elif nums[ind_right] == target: 
                    return ind_right
                else:
                    return -1
            else:   
                ind_mid = (ind_left+ind_right)/2
                if nums[ind_mid] >= target:
                    ind_right = ind_mid
                else:
                    ind_left = ind_mid