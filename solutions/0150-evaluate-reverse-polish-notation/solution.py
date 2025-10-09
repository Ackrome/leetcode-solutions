class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+', '-', '*', '/'}  # set lookup is O(1)
        
        append = stack.append
        pop = stack.pop

        for token in tokens:
            if token in operators:
                b = pop()
                a = pop()
                if token == '+':
                    append(a + b)
                elif token == '-':
                    append(a - b)
                elif token == '*':
                    append(a * b)
                else:
                    append(int(a / b))
            else:
                append(int(token))
        
        return stack[0]
