# coding:utf-8
"""
获取链表的倒数第K个结点
"""


class Solution(object):
    def getKthFromEnd(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        fast = head
        while k and fast:
            fast = fast.next
            k -= 1

        while fast:
            head, fast = head.next, fast.next

        return head
