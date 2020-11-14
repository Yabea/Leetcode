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
        # 找到第N个结点
        slow_node = head
        fast_node = head
        pre = head
        for i in range(n):
            fast_node = fast_node.next

        while fast_node:
            pre = slow_node
            slow_node, fast_node = slow_node.next, fast_node.next

        # 第N个结点找到了
        if slow_node == head:
            return head.next
        else:
            pre.next = slow_node.next
        return head
