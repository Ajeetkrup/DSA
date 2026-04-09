"""
Two Sum Problem - Python Implementations

Author: Ajeet Kumar Upadhyay

Problem Statement:
------------------
Given an array of integers `nums` and an integer `target`,
return indices of the two numbers such that they add up to the target.

Constraints:
- Each input has exactly one solution.
- You may not use the same element twice.
- If no solution exists, return [-1, -1]

------------------------------------------------------------
Approach 1: Brute Force
------------------------------------------------------------
Time Complexity: O(n^2)
Space Complexity: O(1)

Idea:
Check all possible pairs and return indices when sum equals target.
"""


from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

        return [-1, -1]


"""
------------------------------------------------------------
Approach 2: Hash Map (Two Pass)
------------------------------------------------------------
Time Complexity: O(n)
Space Complexity: O(n)

Idea:
1. Store all elements in a hashmap (value -> index)
2. Check if (target - current element) exists
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i in range(len(nums)):
            map[nums[i]] = i

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in map and map.get(diff) != i and map.get(diff) >= 0:
                return [i, map.get(diff)];

        return [-1, -1]
