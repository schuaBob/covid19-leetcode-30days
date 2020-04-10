class Solution:
    def countElements(self, arr: List[int]) -> int:
        arr.sort()
        listSet = list(set(arr))
        t = 0
        for i in listSet:
            n = arr.count(i)
            if i+1 in arr:
                t += n
        return t
