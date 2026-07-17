class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '*', '/']
        for token in tokens:
            if token.replace('-', '').isdigit():
                stack.append(token)
            else:
                dig1, dig2 = int(stack.pop()), int(stack.pop())
                if token == '+': 
                    stack.append(dig1+dig2)
                elif token == '-':
                    stack.append(dig2-dig1)
                elif token == '*':
                    stack.append(dig1*dig2)
                else:
                    stack.append(dig2/dig1)

        result = int(stack.pop())
        return result
                