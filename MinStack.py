class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stk = [None]*50000
        self.ptr = -1

    def push(self, x: int) -> None:
        self.ptr += 1
        self.stk[self.ptr] = x

    def pop(self) -> None:
        if self.ptr >= 0:
            self.ptr -= 1

    def top(self) -> int:
        if self.ptr >= 0:
            return self.stk[self.ptr]

    def getMin(self) -> int:
        if self.ptr >= 0:
            t = float('inf')
            for i in range(self.ptr+1):
                if self.stk[i] < t:
                    t = self.stk[i]
            return t


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
