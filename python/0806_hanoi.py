# coding:utf-8
"""
汉诺塔问题
"""


class Solution(object):
    def hanota(self, A, B, C):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :rtype: None Do not return anything, modify C in-place instead.
        """
        n = len(A)
        self.move(n, A, B, C)

    def move(self, n, A, B, C):
        if n == 1:
            C.append(A.pop())
        else:
            self.move(n - 1, A, C, B)
            self.move(1, A, B, C)
            self.move(n - 1, B, A, C)
