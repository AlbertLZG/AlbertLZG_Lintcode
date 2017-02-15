class Solution:
    """
    @param nums: A list of Integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        # write your code here
        self.ret = []
        if len(nums) == 0:
            return [[]]
        else:
            self._permute(nums, 0)
        return self.ret

    def _permute(self, nums, start):
        if start == len(nums):
            self.ret.append(nums[:])  
        else:
            for i in range(start, len(nums)):
                nums[i], nums[start] = nums[start], nums[i]
                self._permute(nums, start + 1)
                nums[i], nums[start] = nums[start], nums[i]