# coding:utf-8
"""
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:

输入: 123
输出: 321
示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21

注意:

假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
"""


class Solution(object):
    """
    比较基础的想法，依次由低位到高位取数据，并判断返回结果是否溢出 
    """
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        y = abs(x)
        res = 0
        judge = pow(2, 31) - 1 if x > 0 else pow(2, 31)

        while y != 0:
            pop = y % 10
            y /= 10
            res = res * 10 + pop
            if res > judge:
                return 0

        return res if x > 0 else -res
