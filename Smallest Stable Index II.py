"""
You are given an integer array nums of length n and an integer k.

For each index i, define its instability score as max(nums[0..i]) - min(nums[i..n - 1]).

In other words:

max(nums[0..i]) is the largest value among the elements from index 0 to index i.
min(nums[i..n - 1]) is the smallest value among the elements from index i to index n - 1.
An index i is called stable if its instability score is less than or equal to k.

Return the smallest stable index. If no such index exists, return -1.

 

Example 1:

Input: nums = [5,0,1,4], k = 3

Output: 3

Explanation:

At index 0: The maximum in [5] is 5, and the minimum in [5, 0, 1, 4] is 0, so the instability score is 5 - 0 = 5.
At index 1: The maximum in [5, 0] is 5, and the minimum in [0, 1, 4] is 0, so the instability score is 5 - 0 = 5.
At index 2: The maximum in [5, 0, 1] is 5, and the minimum in [1, 4] is 1, so the instability score is 5 - 1 = 4.
At index 3: The maximum in [5, 0, 1, 4] is 5, and the minimum in [4] is 4, so the instability score is 5 - 4 = 1.
This is the first index with an instability score less than or equal to k = 3. Thus, the answer is 3.
"""

class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        min_nums = [0]*len(nums)
        max_nums = [0]*len(nums)

        max_el = float('-inf')
        for i in range(len(nums)):
            if nums[i] > max_el:
                max_el = nums[i]
                max_nums[i] = nums[i]
            else:
                max_nums[i]= max_el
                
        min_el = float('inf')
        for i in range(len(nums)-1, -1, -1):
            if nums[i] < min_el:
                min_el = nums[i]
                min_nums[i] = nums[i]
            else:
                min_nums[i] = min_el

        for i in range(len(nums)):
            score = 0
            
            if i == 0:
                score = nums[i] - min_nums[i]
            elif i > 0 and i < len(nums) - 1:
                score = max_nums[i] - min_nums[i]
            else:
                score = max_nums[i] - nums[i]

            if score <= k:
                return i

        return -1     