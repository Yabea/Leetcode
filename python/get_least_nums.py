# coding:utf-8
"""
最小的K个数
"""


class Solution1(object):
    def getLeastNumbers(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not k:
            return []

        min_k_data = arr[:k]
        total_num = len(arr)

        for i in range(k, total_num):
            if arr[i] < max(min_k_data):
                min_k_data.remove(max(min_k_data))
                min_k_data.append(arr[i])

        return min_k_data


class Solution(object):
    def getLeastNumbers(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        arr.sort()
        return arr[:k]