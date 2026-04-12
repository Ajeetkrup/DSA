"""
📌 Problem: Subarray Sum Equals K

Given an integer array `nums` and an integer `k`,
return the total number of continuous subarrays whose sum equals `k`.

This file contains three approaches:
1. Brute Force (O(n^3))
2. Improved Brute Force (O(n^2))
3. Optimal (Prefix Sum + HashMap) (O(n))
"""

"""
🥉 Approach 1: Brute Force (Using Helper Function)
Time Complexity: O(n^3)
Space Complexity: O(1)
"""

class Solution:
    def sum(self, nums: List[int], i: int, j: int):
        sum = 0

        for l in range(i, j+1):
            sum += nums[l]

        return sum

    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if self.sum(nums, i, j) == k:
                    count += 1

        return count

"""
🥈 Approach 2: Running Sum Optimization
Time Complexity: O(n^2)
Space Complexity: O(1)
"""
   
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0

        for i in range(len(nums)):
            sum = 0
            for j in range(i, len(nums)):
                sum += nums[j]
                if sum == k:
                    count += 1

        return count
    
"""
🥇 Approach 3: Prefix Sum + HashMap
Time Complexity: O(n)
Space Complexity: O(n)

Key Idea:
If prefix_sum - k exists in hashmap,
then a subarray with sum k is found.
"""

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        table = {0: 1}
        prefix_sum = 0

        for num in nums:
            prefix_sum += num

            if (prefix_sum - k) in table:
                count += table[prefix_sum - k]

            table[prefix_sum] = table.get(prefix_sum, 0) + 1

        return count