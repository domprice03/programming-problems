class Solution:
    OPEN_BRACKETS = ['(', '{', '[']
    CLOSE_BRACKETS = [')', '}', ']']
    BRACKET_PAIRS = {x: y for x, y in zip(OPEN_BRACKETS, CLOSE_BRACKETS)}

    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in self.OPEN_BRACKETS:
                stack.append(c)
            elif c in self.CLOSE_BRACKETS:
                if not stack:
                    return False
                if self.BRACKET_PAIRS.get(stack.pop(), "") != c:
                    return False
        if stack:
            return False
        return True
