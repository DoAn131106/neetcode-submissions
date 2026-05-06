class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for paren in s:
            if paren == '(' or paren == '{' or paren == '[':
                stack.append(paren)
                continue
            if len(stack) <= 0:
                return False
            top = stack.pop()
            if paren == ')':
                if top != '(':
                    return False
            elif paren == '}':
                if top != '{':
                    return False
            elif paren == ']':
                if top != '[':
                    return False
            else:
                return False
        return len(stack) == 0