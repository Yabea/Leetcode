# coding:utf-8
"""
desc：回文链表
"""

"""
思路一：暂存链表val至列表，利用列表切片特性进行解决
"""


class Solution1(object):
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


class Solution(object):
    """
    解法二：链表一分为二，反转后半部分，对比
    """
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True

        # 通过获取后半部分列表并进行反转，和前半部分比较来判断回文
        mid_node = self.find_mid(head)
        second_half_list = self.reverse_list(mid_node)
        first_half_list = head

        while first_half_list and second_half_list:
            if first_half_list.val != second_half_list.val:
                return False
            first_half_list = first_half_list.next
            second_half_list = second_half_list.next

        return True

    def find_mid(self, head):
        # 双指针找到中间结点
        tmp_node = head
        slow = tmp_node
        fast = tmp_node

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverse_list(self, head):
        # 反转链表
        pre = None
        cur = head

        while cur:
            next_node = cur.next
            cur.next = pre
            pre = cur
            cur = next_node

        return pre
