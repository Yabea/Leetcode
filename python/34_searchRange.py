# coding:utf-8
"""
在排序数组中查找元素的第一个和最后一个位置
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 O(log n) 级别。

如果数组中不存在目标值，返回 [-1, -1]。

示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]
示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]
"""


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if target not in nums:
            return [-1, -1]
        left = 0
        right = len(nums) - 1
        mid = (right-left) // 2
        if nums[mid] < target:
            left = mid + 1
        if nums[mid] > target:
            right = mid - 1
        while left <= right and nums[left] < target:
                left += 1
        while left <= right and nums[right] > target:
                right -= 1
        return [left, right]
