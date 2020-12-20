# toboggan shop password problem
# data looks like a bunch of lines in no particular order finishing with a newline
import re
import collections
import sys
import itertools

# data = '''
# 1-3 a: abcde
# 1-3 b: cdefg
# 2-9 c: ccccccccc
# '''
# passList = data.strip().splitlines()

passList = open('data/02.txt','r').read().strip().splitlines()

# policy, then the password
# a-b c: foo  a:lowest # times, b:highest # times, the c: character should be in foo password to be valid
# p1: how many passwords are valid according to their policies
# p2: new policy explanation:
# a-b c: foo  a:char position 1 (1-based), b:char position  2, the c: character should be in one of those 2 positions

r = re.compile(r"(\d+)-(\d+) (.): (.+)")
valids = []

def countInStr(source, matchChar):
    return len(re.findall(matchChar, source))
        

for pl in passList:
    m = r.search(pl)
    minC, maxC, pchar, password = m.groups()
    minC = int(minC)
    maxC = int(maxC)

    if minC <= countInStr(password, pchar) <= maxC:
        valids.append(pl)

print("Part 1: ", len(valids))
valids = []

for pl in passList:
    m = r.search(pl)
    pos1, pos2, pchar, password = m.groups()
    pos1 = int(pos1) - 1
    pos2 = int(pos2) - 1
    
    if bool(password[pos1] == pchar) ^ bool(password[pos2] == pchar):
        valids.append(pl)
    
print("Part 2: ", len(valids))