class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for tk in tokens:
            if tk == '-' or tk == '*' or tk == '/' or tk == '+':
                secondupperand = int(stack.pop())
                firstupperand = int(stack.pop())
                if tk == '-':
                    stack.append(firstupperand - secondupperand)
                if tk == '*':
                    stack.append(firstupperand * secondupperand)
                if tk == '/':
                    stack.append(int(firstupperand / secondupperand))
                if tk == '+':
                    stack.append(firstupperand + secondupperand)
            else:
                stack.append(tk)
        return int(stack[0])