# coding:utf-8
"""
打家劫舍
"""


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_nums = len(nums)

        for i in range(2, len_nums):
            nums[i] = nums[i] + max(nums[:i - 1])

        return max(nums)
