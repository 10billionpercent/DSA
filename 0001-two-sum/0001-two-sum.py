class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        diffs = {}
        found = False
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in diffs:
                return i, diffs[diff]
            diffs[nums[i]] = i

