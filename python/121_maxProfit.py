# coding:utf-8
"""
买卖股票的最佳时机
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。

注意：你不能在买入股票前卖出股票。
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        if prices:
            min_prices = max(prices)
            for i in prices:
                if i < min_prices:
                    min_prices = i
                elif (i-min_prices) > max_profit:
                    max_profit = i - min_prices
        return max_profit
