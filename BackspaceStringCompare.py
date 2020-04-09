class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        Ls = [list(S), list(T)]
        for L in Ls:
            while L.count('#') > 0:
                if L[0] == '#':
                    L.pop(0)
                else:
                    i = L.index('#')
                    L.pop(i)
                    L.pop(i-1)
        return True if Ls[0] == Ls[1] else False
