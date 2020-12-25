# Day 6: Custom Customs 
from collections import defaultdict
data = '''abc

a
b
c

ab
ac

a
a
a
a

b''' 

qList = data.strip().split('\n\n')
#qList = open('data/06.txt','r').read().strip().split('\n\n')

# given:
# 1. each row is an individual's question for which they answered yes
# adjacent data rows are in same group, an extra newline separates 
# groups
# 2. question letters will be encountered in any order (not alpha)
#
# part 1: sum of distinct questions each group answered(yes).  Test input should
# return 11.#
# part 2: sum of distinct questions for each everyone in group answered(yes)

p1 = []
p2 = []
for group in qList:
    groupQuestFreq = defaultdict(int)
    groupEntries = 0
    for entry in group.split():
        groupEntries += 1
        for qLetter in list(entry):
            groupQuestFreq[qLetter] += 1
    p1.append(groupQuestFreq.keys())
    p2.append([x for x in groupQuestFreq.keys() 
        if groupQuestFreq[x] == groupEntries])
    
print("Part 1: ", sum([len(x) for x in p1]))
print("Part 2: ", sum([len(x) for x in p2]))