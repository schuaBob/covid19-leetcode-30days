class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroes = nums.count(0)
        temp = [0 for i in range(zeroes)]
        while zeroes > 0:
            nums.remove(0)
            zeroes -= 1
        nums.extend(temp)
