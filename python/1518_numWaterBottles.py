# coding:utf-8
"""
换酒问题
小区便利店正在促销，用 numExchange 个空酒瓶可以兑换一瓶新酒。你购入了 numBottles 瓶酒。

如果喝掉了酒瓶中的酒，那么酒瓶就会变成空的。

请你计算 最多 能喝到多少瓶酒。
"""


# 迭代
class Solution1(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        ret_data = numBottles

        if numBottles < numExchange:
            return ret_data

        empty_bottles = numBottles

        while empty_bottles >= numExchange:
            tmp_bottle = empty_bottles // numExchange
            empty_bottles = empty_bottles % numExchange + tmp_bottle
            ret_data += tmp_bottle

        return ret_data


# 递归
class Solution2(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        if numBottles < numExchange:
            return numBottles

        numBottles = numBottles - numExchange + 1

        return numExchange + self.numWaterBottles(numBottles, numExchange)
