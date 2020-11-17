# coding:utf-8
"""
 搜索二维矩阵
"""


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)

        for i in range(m):
            tmp_list = matrix[i]
            if not tmp_list or target > tmp_list[-1]:
                continue
            if target < tmp_list[0]:
                return False
            if target in tmp_list:
                return True

        return False
