# coding:utf-8
"""
desc: 回文数
"""


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # total_num = len(str(x))
        # mid = total_num // 2 if total_num % 2 == 0 else total_num // 2 + 1
        # return str(x)[:mid] == str(x)[-mid:][::-1]
        return str(x) == str(x)[::-1]
