# coding:utf-8
"""
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且 n 的值至少为 2。
"""


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        left, right = 0, len(height) - 1
        while left < right:
            left_value = height[left]
            right_value = height[right]
            max_area = max((right-left) * min(left_value, right_value), max_area)
            if left_value <= right_value:
                left += 1
            if left_value >= right_value:
                right -= 1
        return max_area
