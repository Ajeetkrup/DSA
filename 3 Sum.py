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