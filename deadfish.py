import sys

class DeadfishError(Exception):
    def __init__(self, message):
        print(message)
        sys.exit(1)

p = None
if '-p' in sys.argv:
    p = sys.argv[sys.argv.index('-p')+1]

v_o = False
v_t = True
if '-v' in sys.argv:
    v_o = 'o' in sys.argv[sys.argv.index('-v')+1]
    v_t = 't' in sys.argv[sys.argv.index('-v')+1]

c_o = True
c_x = False
if '-c' in sys.argv:
    c_o = 'o' in sys.argv[sys.argv.index('-c')+1]
    c_x = 'x' in sys.argv[sys.argv.index('-c')+1]

w_e = False
w_o = False
w_O = False
w_r = False
if '-w' in sys.argv:
    w_e = 'e' in sys.argv[sys.argv.index('-w')+1]
    w_o = 'o' in sys.argv[sys.argv.index('-w')+1]
    w_O = 'O' in sys.argv[sys.argv.index('-w')+1]
    w_r = 'r' in sys.argv[sys.argv.index('-w')+1]

cmds = {'i': '', 'd': '', 's': '', 'o': '', 'c': '', 'h': '', 'w': '', '(': '', ')': '', '{': '', '}': ''}
if v_t:
    if c_o:
        cmds['i'] += 'i'
        cmds['d'] += 'd'
        cmds['s'] += 's'
        cmds['o'] += 'o'
        cmds['c'] += 'c'
        cmds['h'] += 'h'
        cmds['w'] += 'w'
        cmds['('] += '('
        cmds[')'] += ')'
        cmds['{'] += '{'
        cmds['}'] += '}'
    if c_x:
        cmds['i'] += 'x'
        cmds['d'] += 'd'
        cmds['s'] += 'k'
        cmds['o'] += 'C'
        cmds['c'] += 'c'
        cmds['h'] += 'D'
        cmds['w'] += 'k'
        cmds['('] += 'x'
        cmds[')'] += 'D'
        cmds['{'] += 'X'
        cmds['}'] += 'D'
elif v_o:
    if c_o:
        cmds['i'] += 'i'
        cmds['d'] += 'd'
        cmds['s'] += 's'
        cmds['o'] += 'o'
    if c_x:
        cmds['i'] += 'x'
        cmds['d'] += 'd'
        cmds['s'] += 'k'
        cmds['o'] += 'c'

def execute(acc, prog, i=0, recursion=False):
    brackets = 0
    while i < len(prog):
        ch = prog[i]

        if ch in cmds['i']:
            acc += 1
        elif ch in cmds['d']:
            acc -= 1
        elif ch in cmds['s']:
            acc *= acc
        elif ch in cmds['w']:
            print('Hello, World!', end='')
        elif ch in cmds['(']:
            if acc == 0:
                i += 1
                while i < len(prog):
                    ch = prog[i]
                    if ch in cmds[')']:
                        break
                    i += 1
                if i >= len(prog):
                    break
            else:
                brackets += 1
        elif ch in cmds['{']:
            for _ in range(0, 9):
                acc = execute(acc, prog, i + 1, True)[0]
            state = execute(acc, prog, i + 1, True)
            acc = state[0]
            i = state[1]
        elif bool(brackets) and ch in cmds[')']:
            brackets -= 1
        elif recursion and ch in cmds['}']:
            return [acc, i]
        elif ch in cmds['h']:
            print('\nLong live the fish!')
            sys.exit(0)
        elif w_r and ch == 'r':
            acc = 0
        elif not (ch in cmds['o'] or ch in cmds['c']):
            if w_e:
                raise DeadfishError('\nInvalid character {} at index {}'.format(ch, i))
            else:
                print('\n', end='')

        if (acc == -1 or acc == 256) or (w_O and (acc < 0 or acc > 255)):
            if w_o:
                raise DeadfishError('\nOverflow at char {} (Index {}) accumulator = {}'.format(ch, i, acc))
            else:
                acc = 0

        if ch in cmds['o']:
            print(acc, end='')
        elif ch in cmds['c']:
            print(chr(acc), end='')
        i += 1
    return [acc, i]

print('Deadfish~ interpreter version 0.13')

acc = 0
if bool(p):
    acc = execute(acc, p)[0]
while True:
    inp = input('\n>> ')
    acc = execute(acc, inp)[0]
