# coding:utf-8
"""
desc：回文链表
"""

"""
思路一：暂存链表val至列表，利用列表切片特性进行解决
"""


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        tmp_list = []
        while head:
            tmp_list.append(head.val)
            head = head.next

        if tmp_list == tmp_list[::-1]:
            return True
        return False

