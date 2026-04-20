class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [0]*len(nums)

        curr = 1
        for i in range(1, len(nums)):
            curr *= nums[i-1]
            ans[i] = curr

        suff, ans[0] = 1, 1
        for i in range(len(nums)-2, -1, -1):
            suff *= nums[i+1]
            ans[i] *= suff

        return ans