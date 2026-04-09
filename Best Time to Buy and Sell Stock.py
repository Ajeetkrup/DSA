"""
Best Time to Buy and Sell Stock - Python Implementation

Author: Ajeet Kumar Upadhyay

Problem Statement:
------------------
You are given an array `prices` where `prices[i]` is the price of a stock on day `i`.

You want to maximize your profit by choosing:
- One day to buy the stock
- A different day in the future to sell that stock

Return the maximum profit you can achieve.
If no profit is possible, return 0.

------------------------------------------------------------
Approach 1: Brute Force
------------------------------------------------------------
Time Complexity: O(n^2)
Space Complexity: O(1)

Idea:
Check every pair (buy day, sell day) and track the maximum profit.
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                profit = max(prices[j]-prices[i], profit)

        return profit

