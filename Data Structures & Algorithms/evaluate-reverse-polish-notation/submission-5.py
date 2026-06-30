from math import trunc

class Solution:
    OPS = {"+", "-", "*", "/"}
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for tok in tokens:
            if tok in self.OPS:
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                match tok:
                    case "+":
                        stack.append(num2 + num1)
                    case "-":
                        stack.append(num2 - num1)
                    case "*":
                        stack.append(num2 * num1)
                    case "/":
                        stack.append(trunc(num2 / num1))
            else:
                stack.append(tok)
        return int(stack[0])