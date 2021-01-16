# coding:utf-8
"""
数组加一
"""


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits[-1] += 1
        for i in range(1, len(digits)):
            if digits[-i] < 10:
                return digits
            digits[-i], digits[-(i + 1)] = 0, digits[-(i + 1)] + 1

        if digits[0] == 10:
            digits[0] = 0
            digits = [1] + digits

        return digits
