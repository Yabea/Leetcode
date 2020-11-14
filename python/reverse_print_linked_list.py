# coding:utf-8
"""
从尾到头打印链表
"""


# 栈
class Solution1(object):
    def reversePrint(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        ret_data = []

        tmp_point = head
        while tmp_point:
            ret_data.insert(0, tmp_point.val)
            tmp_point = tmp_point.next
        return ret_data


# 递归
class Solution2(object):
    def reversePrint(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        ret_data = []

        tmp_point = head
        while tmp_point:
            ret_data.insert(0, tmp_point.val)
            tmp_point = tmp_point.next
        return ret_data
