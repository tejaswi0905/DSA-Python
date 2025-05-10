def maxProfit(prices) -> int:
    l = 0
    r = 1
    max_profit = 0
    while r<len(prices):
        if prices[r]<prices[l]:
            l = r
        else:
            current = prices[r] - prices[l]
            if current>max_profit:
                max_profit = current
        r+=1
    return max_profit

print(maxProfit(prices = [7,1,5,3,6,4]))

"""
the question is: LEETCODE - 121
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

"""