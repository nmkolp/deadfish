import sys

class DeadfishError(Exception):
    def __init__(self, message):
        print(message)
        sys.exit(1)

prog = None
if '-p' in sys.argv:
    prog = sys.argv[sys.argv.index('-p')+1]

variant_tilde = True
if '-v' in sys.argv:
    variant_tilde = not ('o' in sys.argv[sys.argv.index('-v')+1] and not ('t' in sys.argv[sys.argv.index('-v')+1]))

cmd_original = True
cmd_xkdc = False
if '-c' in sys.argv:
    cmd_original = 'o' in sys.argv[sys.argv.index('-c')+1]
    cmd_xkdc = 'x' in sys.argv[sys.argv.index('-c')+1]

wimp_errors = False
wimp_overflow = False
wimp_true_overflow = False
wimp_reset = False
if '-w' in sys.argv:
    wimp_errors = 'e' in sys.argv[sys.argv.index('-w')+1]
    wimp_overflow = 'o' in sys.argv[sys.argv.index('-w')+1]
    wimp_true_overflow = 'O' in sys.argv[sys.argv.index('-w')+1]
    wimp_reset = 'r' in sys.argv[sys.argv.index('-w')+1]

def execute(acc, prog, i=0, recursion=False):
    while i < len(prog):
        char = prog[i]
        if (cmd_original and char == 'i') or (cmd_xkdc and char == 'x'):
            acc += 1
        elif char == 'd':
            acc -= 1
        elif (cmd_original and char == 's') or (cmd_xkdc and char == 'k'):
            acc *= acc
        elif variant_tilde and ((cmd_original and char == 'h') or (not recursion and cmd_xkdc and char == 'D')):
            print('\nLong live the fish!')
            sys.exit(0)
        elif wimp_reset and char == 'r':
            acc = 0
        elif variant_tilde and ((cmd_original and char == 'w') or (cmd_xkdc and char == 'K')):
            print('Hello, World!', end='')
        elif variant_tilde and recursion and ((cmd_original and char == '}') or (cmd_xkdc and char == 'D')):
            return [acc, i]
        elif variant_tilde and ((cmd_original and char == '{') or (cmd_xkdc and char == 'X')):
            for _ in range(0, 9):
                state = execute(acc, prog, i + 1, True)
                acc = state[0]
            state = execute(acc, prog, i + 1, True)
            acc = state[0]
            i = state[1]
        elif variant_tilde and ((cmd_original and char == '(') or (cmd_xkdc and char == 'x')):
            if acc == 0:
                i += 1
                while i < len(prog):
                    char = prog[i]
                    if (cmd_original and char == ')') or (cmd_xkdc and char == 'D'):
                        break
                    i += 1
                if i >= len(prog):
                    break
        elif not ((variant_tilde and cmd_original and char in ['o', 'c']) or (variant_tilde and cmd_xkdc and char in ['C', 'c']) or (not variant_tilde and cmd_original and char == 'o') or (not variant_tilde and cmd_xkdc and char == 'c')):
            if wimp_errors:
                raise DeadfishError('\nInvalid character {} at index {}'.format(char, i))
            else:
                print('\n', end='')
        if (acc == -1 or acc == 256) or (wimp_true_overflow and (acc < 0 or acc > 255)):
            if wimp_overflow:
                raise DeadfishError('\nOverflow at char {} (Index {}) accumulator = {}'.format(char, i, acc))
            else:
                acc = 0
        if (cmd_original and char == 'o') or (cmd_xkdc and char == 'c' and not variant_tilde) or (cmd_xkdc and char == 'C' and variant_tilde):
            print(acc, end='')
        elif variant_tilde and char == 'c':
            print(chr(acc), end='')
        i += 1
    return [acc, i]

acc = 0

print('Deadfish~ interpreter version 0.12')

while True:
    if not bool(prog):
        prog = input('\n>> ')
    state = execute(acc, prog)
    acc = state[0]
    prog = None
    
