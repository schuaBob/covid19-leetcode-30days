class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        windowSum = nums[0]
        maxSum = nums[0]
        for i in nums[1:]:
            windowSum = max(windowSum+i, i)
            maxSum = max(windowSum, maxSum)
        return maxSum
