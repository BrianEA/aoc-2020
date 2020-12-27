# Day 8: Handheld halting
import re 
import sys
# data = '''nop +0
# acc +1
# jmp +4
# acc +3
# jmp -3
# acc -99
# acc +1
# jmp -4
# acc +6
# ''' 

# ogInstructions = data.strip().splitlines()
ogInstructions = open('data/08.txt','r').read().strip().splitlines()

# part 1: what is the value in the accumulator immediately before any instruction is executed a second time
# part 2: if we try flipping a single nop or jmp to jmp or nop, across the instruction set, one such change
#   will result in attempting to go one instruction past the end of the program.  In such a case, 
#   the program should terminate.  What is value in the accumulator in this case?

programLength = len(ogInstructions)
p1done = False
p2counter = 0

# length + 1 max iterations - once unchanged, then once for every instruction
while p2counter < programLength + 1:
    visited = []
    acc = 0
    idx = 0
    instructions = ogInstructions[:]
    
    if p2counter > 0:
        # we're only testing variations of nop vs jump
        if instructions[p2counter-1].startswith("acc"):
            p2counter += 1
            continue
        else:
            i = instructions[p2counter-1]
            if i.startswith('nop'):
                instructions[p2counter-1] = "jmp "+i[4:]
            elif i.startswith('jmp'):
                instructions[p2counter-1] = "nop "+i[4:]
    while 1:
        if idx in visited: 
            if not p1done:
                print("Part 1: ", acc)
                p1done = True
            break

        if idx == programLength:
            print("Part 2: ", acc)
            sys.exit(0)

        visited.append(idx)
        opcode, val = instructions[idx].split()

        if opcode == 'jmp':
            idx += int(val)
        else:
            if opcode == 'acc':
                acc += int(val)    
            idx +=1     

    p2counter += 1