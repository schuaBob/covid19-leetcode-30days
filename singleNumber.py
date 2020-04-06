class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        temp = dict()
        for i in nums:
            i = str(i)
            if i not in temp:
                temp[i] = 1
            elif temp[i] < 2:
                temp[i] += 1
        for s in temp:
            if temp[s] == 1:
                return s
