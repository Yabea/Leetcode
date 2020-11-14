# coding:utf-8

"""
反转链表
"""


# 迭代
class Solution1(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        tmp_point = head
        pre = None

        while tmp_point:
            next_point = tmp_point.next
            tmp_point.next = pre
            pre = tmp_point
            tmp_point = next_point

        return pre


# 递归
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        tmp_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return tmp_head



