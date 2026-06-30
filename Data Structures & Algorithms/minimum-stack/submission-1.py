class MinStack:

    def __init__(self):
        self._stack = []
        self._min = []

    def push(self, val: int) -> None:
        self._stack.append(val)
        if not self._min or val <= self._min[-1]:
            self._min.append(val)

    def pop(self) -> None:
        popped = self._stack.pop()
        if popped == self._min[-1]:
            self._min.pop()

    def top(self) -> int:
        return self._stack[-1]

    def getMin(self) -> int:
        return self._min[-1]
