# coding:utf-8
"""
链表的中间结点
"""


class Solution1(object):
    """
    单指针
    """
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        list_num = 0
        tmp_point = head

        while tmp_point:
            list_num += 1
            tmp_point = tmp_point.next

        mid = list_num // 2

        for i in range(mid):
            head = head.next

        return head


class Solution(object):
    """
    双链表
    """
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = head

        while fast and fast.next:
            head = head.next
            fast = fast.next.next
        return head