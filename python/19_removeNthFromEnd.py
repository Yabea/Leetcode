# coding:utf-8
"""
 删除链表的倒数第N个节点
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：

给定的 n 保证是有效的。
"""


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # 先找到倒数第N个节点
        first_head = head
        second_head = head
        tmp_num = 1
        while first_head.next != None:
            first_head = first_head.next
            if tmp_num > n:
                second_head = second_head.next
            tmp_num += 1
        # 删除第n个节点
        if tmp_num > n:
            second_head.next = second_head.next.next
        else:
            return head.next
        return head
