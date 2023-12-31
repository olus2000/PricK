def entry(s, t):
    s = list(s)
    perms = [0] * len(s)
    res = set()
    while True:
        #         print(s, end='')
        #         print([str(i) for i in perms])
        #         print()
        r, d = eval(s)
        res.update(r)
        skip_after(d, s)
        while d <= len(s):
            if d % 2 == 1:
                s[-d], s[-1] = s[-1], s[-d]
            else:
                s[-d], s[-perms[-d]-1] = s[-perms[-d]-1], s[-d]
            perms[-d] += 1
            if perms[-d] < d: break
            perms[-d] = 0
            d += 1
        else: break
    return res, min(map(lambda x: (abs(t - x), x), res))[1]


def skip_after(d, s):
    if d % 2 == 0 or d < 3: return
    x = s[-d+1]
    for i in range(-d+1, -1):
        s[i] = s[i+1]
    s[-1] = x


def eval(s):
    stack = []
    res = set()
    for i, c in enumerate(s):
        if c in '0123456789':
            stack.append(int(c))
        elif len(stack) < 2:
            return res, len(s) - i
        elif c == '+':
            stack.append(stack.pop() + stack.pop())
        elif c == '*':
            stack.append(stack.pop() * stack.pop())
        elif c == '-':
            a, b = stack.pop(), stack.pop()
            if b < a: return res, len(s) - i
            stack.append(b - a)
        elif c == '/':
            a, b = stack.pop(), stack.pop()
            if a == 0 or b / a % 1 != 0: return res, len(s) - i
            stack.append(b // a)
        else:
            raise Exception(c, s)
        res.add(stack[-1])
    return res, 1
