def calculate(self, s: str) -> int:
    s = s.replace(" ", "")
    s += " "
    stack = []
    sign = '+'
    num = 0

    for c in s:
        if c.isdigit():
            num = 10 * num + int(c)
        else:
            if sign == '+':
                stack.append(num)
            elif sign == '-':
                stack.append(-num)
            elif sign == '*':
                stack[-1] = stack[-1] * num
            elif sign == '/':
                stack[-1] = int(stack[-1] / float(num))
            num = 0
            sign = c
    return sum(stack)