# naive

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: 
            return 0

        nums.sort()

        count = 1
        maxLen = 1

        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] == 1:
                count += 1
                if count > maxLen:
                    maxLen = count
            elif nums[i] == nums[i-1]:
                continue
            else:
                count = 1

        return maxLen 

# optimized 
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1: 
            return len(nums)

        numHash = set(nums)
        maxLen = 1

        for i in numHash:
            if i-1 not in numHash:
                count = 1
                while i+count in numHash:
                    count += 1

                maxLen = max(maxLen, count)

        return maxLen 
