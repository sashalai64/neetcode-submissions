class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        opt = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: int(float(x) / y)
        }

        res = []

        for t in tokens:
            if t in opt:
                y = res.pop()
                x = res.pop()
                res.append(opt[t](x, y))
            else:
                res.append(int(t))
        
        return res[-1]