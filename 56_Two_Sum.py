class Solution:
    """
    @param numbers : An array of Integer
    @param target : target = numbers[index1] + numbers[index2]
    @return : [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        # write your code here
        _add = {}
        for i in range(len(numbers)):
            if numbers[i] in _add:
                return [_add[numbers[i]], i+1]
            else:
                _add[target-numbers[i]] = i+1