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

def countInStr(source, matchChar):
    return len(re.findall(matchChar, source))
        
p1valids = []
p2valids = []
for pl in passList:
    m = r.search(pl)
    n1, n2, pchar, password = m.groups()
    n1 = int(n1)
    n2 = int(n2)

    if n1 <= countInStr(password, pchar) <= n2:
        p1valids.append(pl)
    if bool(password[n1-1] == pchar) ^ bool(password[n2-1] == pchar):
        p2valids.append(pl)
    
print("Part 1: ", len(p1valids))
print("Part 2: ", len(p2valids))