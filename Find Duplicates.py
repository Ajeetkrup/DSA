"""
Approach 1: Sorting

Description:
- Sort the input array.
- Traverse once and check if any adjacent elements are equal.
- If yes → duplicate exists.

Time Complexity:
- O(n log n) due to sorting.

Space Complexity:
- O(1) (in-place sort, ignoring Python’s internal overhead).

Pros:
- Simple and uses no extra data structures.

Cons:
- Slower than optimal solution due to sorting.
- Modifies the input array.
"""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True

        return False
    
"""
Approach 2: HashSet (Optimal)

Description:
- Use a set to track seen elements.
- Iterate through the array:
    - If element already in set → duplicate found.
    - Else add it to the set.

Time Complexity:
- O(n)

Space Complexity:
- O(n)

Pros:
- Fastest approach.
- Does not require sorting.

Cons:
- Uses extra space.
"""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for i in range(len(nums)):
            if nums[i] in seen:
                return True

            seen.add(nums[i])

        return False