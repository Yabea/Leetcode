# coding:utf-8
"""
相交链表
"""


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None

        tmp_head_a = headA
        tmp_head_b = headB

        while tmp_head_a != tmp_head_b:
            tmp_head_a = tmp_head_a.next if tmp_head_a else headB
            tmp_head_b = tmp_head_b.next if tmp_head_b else headA

        return tmp_head_a
