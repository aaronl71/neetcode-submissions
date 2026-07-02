class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        operands = ["-", "+", "*", "/"]
        for i in range(len(tokens)):
            if tokens[i] not in operands:
                stk.append(int(tokens[i]))
            if tokens[i] == "+":
                a = stk.pop()
                b = stk.pop()
                stk.append(int(a + b))
            if tokens[i] == "-":
                a = stk.pop()
                b = stk.pop()
                stk.append(int(b - a))
            if tokens[i] == "*":
                a = stk.pop()
                b = stk.pop()
                stk.append(int(a * b))
            if tokens[i] == "/":
                a = stk.pop()
                b = stk.pop()
                stk.append(int(b / a))
            
        return stk[0]
                
                



                

