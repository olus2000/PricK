#! /usr/bin/python3
from sys import argv

def interpret(s):
    program = s.split()
    stack = []
    aux = []
    memory = []

    def pop(stack=stack):
        if len(stack):
            return stack.pop()
        return 0

    def peek(stack=stack):
        if len(stack):
            return stack[-1]
        return 0

    def get(n):
        if len(memory) > n:
            return memory[n]
        return 0
    
    def set(n, v):
        nonlocal memory
        memory += [0] * (n - len(memory) + 1)
        memory[n] = v

    def swap():
        a, b = pop(), pop()
        stack.append(a)
        stack.append(b)

    def over():
        if len(stack) > 1:
            return stack.append(stack[-2])
        stack.append(0)

    def rot():
        a, b, c = pop(), pop(), pop()
        stack.append(b)
        stack.append(a)
        stack.append(c)

    def div():
        a, b = pop(), pop()
        stack.append(b // max(a, 1))

    words = {
            "#"     : 0,
            "++"    : lambda: stack.append(pop() + 1),
            "!"     : lambda: set(pop(), pop()),
            "@"     : lambda: stack.append(get(pop())),
            "dup"   : lambda: stack.append(peek()),
            "drop"  : pop,
            "swap"  : swap,
            "over"  : over,
            "rot"   : rot,
            "+"     : lambda: stack.append(pop() + pop()),
            "--"    : lambda: stack.append(max(0, pop() - 1)),
            "-"     : lambda: stack.append(max(0, -pop() + pop())),
            "*"     : lambda: stack.append(pop() * pop()),
            "/"     : div,
            "!="    : lambda: stack.append(int(pop() != pop())),
            ">aux"  : lambda: aux.append(pop()),
            "aux>"  : lambda: stack.append(pop(aux)),
            "aux@"  : lambda: stack.append(peek(aux)),
            "$"     : lambda: print(stack, aux, memory, sep="\n")
    }

    i = 0

    def parse_body(delim):
        nonlocal i
        body = []
        while True:
            if (i >= len(program) and delim == ":") or program[i] == delim:
                return body
            elif program[i] in ("|", "]", ":"):
                raise Exception(i, program[i])
            elif program[i] == "[":
                i += 1
                cond = parse_body("|")
                i += 1
                loop = parse_body("]")
                body.append((cond, loop))
            elif program[i] in words:
                body.append(words[program[i]])
            elif program[i].isnumeric():
                body.append(int(program[i]))
            i += 1


    while True:
        body = parse_body(":")
        if i >= len(program):
            break
        if program[i] == ":":
            words[program[i+1]] = body
        else:
            raise Exception(i, program[i:])
        i += 2

    def exec(x):
        if callable(x):
            x()
        elif isinstance(x, list):
            for i in x: exec(i)
        elif isinstance(x, tuple):
            bound = pop()
            while (exec(x[0]) or pop() > 0) and bound > 0:
                exec(x[1])
                bound -= 1
        elif isinstance(x, int):
            stack.append(x)
        else:
            raise Exception(x)

    exec(body)

    return memory, aux, stack


if __name__ == '__main__':
    with open(argv[1]) as f:
        s = f.read()
    mem, aux, stk = interpret(s)
    print(mem)
    print(aux)
    print(stk)
