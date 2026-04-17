"""
Approach 1: Brute Force (Three Nested Loops)

Description:
- Try all possible triplets (i, j, k) such that i < j < k.
- Check if their sum is zero.
- Sort each triplet and use a set to avoid duplicates.

Time Complexity:
- O(n^3) for generating all triplets.

Space Complexity:
- O(n) for storing unique triplets in a set.

Pros:
- Simple and easy to understand.

Cons:
- Very inefficient for large inputs.
- Extra overhead of sorting each triplet and using a set.
"""
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        seen = set()

        for i in (range(len(nums))):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    triplet = [nums[i], nums[j], nums[k]]
                    triplet.sort()

                    if tuple(triplet) not in seen and i != j and j!= k and k!= i and (nums[i] + nums[j] + nums[k] == 0):
                        result.append([nums[i], nums[j], nums[k]])
                        seen.add(tuple(triplet))

        return result

"""
Approach 2: HashMap + Two Loops

Description:
- Store elements in a hashmap (value -> index).
- Fix two numbers (i, j) and compute the third as -(nums[i] + nums[j]).
- Check if this value exists in the hashmap.
- Use a set to avoid duplicate triplets.

Time Complexity:
- O(n^2) for two nested loops.

Space Complexity:
- O(n) for hashmap and set.

Pros:
- Better than brute force.

Cons:
- Hashmap stores only one index per value → may miss valid duplicates.
- Still requires a set to handle duplicate triplets.
- Less reliable than optimal approach.
"""
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        seen = set()
        map_list = {}

        for i in (range(len(nums))):
            map_list[nums[i]] = i

        for i in (range(len(nums))):
            for j in range(i+1, len(nums)):
                k = map_list.get(-(nums[i]+nums[j]))
                if k != None and k != i and i != j and j != k:
                    triplet = [-(nums[i]+nums[j]), nums[i], nums[j]]
                    triplet.sort()

                    if tuple(triplet) not in seen:
                        result.append([nums[i], nums[j], -(nums[i]+nums[j])])
                        seen.add(tuple(triplet))

        return result

"""
Approach 3: Sorting + Two Pointers (Optimal)

Description:
- Sort the array.
- Fix one element and use two pointers (left, right) to find remaining two.
- Move pointers based on sum comparison with zero.
- Skip duplicates to ensure unique triplets.

Time Complexity:
- O(n^2)

Space Complexity:
- O(1) (excluding output)

Pros:
- Most efficient and standard interview solution.
- No extra set or hashmap needed.
- Handles duplicates elegantly.

Cons:
- Requires sorting (modifies input).
"""
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        nums.sort()
       
        for i in range(len(nums)):
            if i > 0 and nums[i-1] == nums[i]:
                continue

            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left+1]:
                        left += 1

                    while left < right  and nums[right] == nums[right-1]:
                        right -= 1

                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return result