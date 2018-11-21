import sys

class DeadfishError(Exception):
    def __init__(self, message):
        print(message)
        sys.exit(1)

prog = sys.argv[sys.argv.index('-p')+1] if '-p' in sys.argv else None
strict = '-strict' in sys.argv or '-s' in sys.argv
strict_overflow = '-overflow' in sys.argv or '-o' in sys.argv

def execute(acc, prog, i=0, recursion=False):
    while i < len(prog):
        char = prog[i]
        if char in ['i','x']:
            acc += 1
        elif char == 'd':
            acc -= 1
        elif char in ['s', 'k']:
            acc *= acc
        elif char == 'h':
            print('\nLong live the fish!')
            sys.exit(0)
        elif char == 'r':
            acc = 0
        elif char == 'w':
            print('Hello, World!', end='')
        elif recursion and char == '}':
            return [acc, i]
        elif char == '{':
            for _ in range(0, 9):
                state = execute(acc, prog, i + 1, True)
                acc = state[0]
            state = execute(acc, prog, i + 1, True)
            acc = state[0]
            i = state[1]
        elif char == '(':
            if acc == 0:
                i += 1
                while i < len(prog):
                    char = prog[i]
                    if char == ')':
                        break
                    i += 1
                if i >= len(prog):
                    break
        elif not char in ['o', 'c']:
            if strict:
                raise DeadfishError('\nInvalid character {} at index {}'.format(char, i))
            else:
                print('\n', end='')
        if acc == -1 or acc == 256:
            if strict_overflow:
                raise DeadfishError('\nOverflow at char {} (Index {}) accumulator = {}'.format(char, i, acc))
            else:
                acc = 0
        if char == 'o':
            print(acc, end='')
        elif char == 'c':
            print(chr(acc), end='')
        i += 1
    return [acc, i]

acc = 0

print('Deadfish~ interpreter version 0.1')

while True:
    if not bool(prog):
        prog = input('\n>> ')
    state = execute(acc, prog)
    acc = state[0]
    prog = None
    
