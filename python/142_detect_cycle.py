# coding:utf-8


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = head
        slow = head

        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

            if slow == fast:
                tmp_point = head
                while tmp_point != slow:
                    tmp_point, slow = tmp_point.next, slow.next
                return slow

        return None
