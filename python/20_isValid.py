# coding:utf-8
"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。
"""


# 解法一
class Solution1(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        while "{}" in s or "()" in s or "[]" in s:
            s = s.replace("()", "")
            s = s.replace("{}", "")
            s = s.replace("[]", "")
        return s == ""


# 解法二
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        data = {')': '(', '}': '{', ']': '['}
        tmp_stack = []
        for item in s:
            if item in data.values():
                tmp_stack.append(item)
            if item in data.keys():
                if tmp_stack and data[item] == tmp_stack[-1]:
                    tmp_stack.pop()
                else:
                    return False
        return tmp_stack == []
