"""
给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。

你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。

返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。

示例 1：
输入：[7,1,5,3,6,4]
输出：5
解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。

示例 2：
输入：prices = [7,6,4,3,1]
输出：0
解释：在这种情况下, 没有交易完成, 所以最大利润为 0。

思路：总是用右侧的最大值减去左侧的最小值，只需要更新最小值，利润最大值随当前值与最小值的差计算同步更新即可，只需要一遍循环

"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # max = 0
        # for i in range(1,len(prices)):
        #     for j in range(i+1,len(prices)):
        #         if  prices[j]-prices[i]>max:
        #             max = prices[j]-prices[i]
        # if max==0:
        #     return 0
        # else:
        #     return max

        # 优化： 思路，找到最大值和最小值做差就可以找到最好的
        # 时间复杂度O(n),空间O(1)
        # 初始化最小价格和最大利润
        min_price = float('inf')  # 其初始值设置为正无穷大（Infinity）。这是 Python 处理最小值问题的一种常见方法。
        max_profit = 0

        # 遍历价格数组
        for price in prices:
            # 更新最小价格
            # 条件没达到，不更新最小值也是维持之前的选值
            if price < min_price:
                min_price = price
            # 计算当前利润
            current_profit = price - min_price
            # 更新最大利润
            if current_profit > max_profit:
                max_profit = current_profit

        return max_profit
