# Day 7: Handy Haversacks
import re 

# data = '''light red bags contain 1 bright white bag, 2 muted yellow bags.
# dark orange bags contain 3 bright white bags, 4 muted yellow bags.
# bright white bags contain 1 shiny gold bag.
# muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
# shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
# dark olive bags contain 3 faded blue bags, 4 dotted black bags.
# vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
# faded blue bags contain no other bags.
# dotted black bags contain no other bags.''' 

# 2nd p2 sample
# data = '''shiny gold bags contain 2 dark red bags.
# dark red bags contain 2 dark orange bags.
# dark orange bags contain 2 dark yellow bags.
# dark yellow bags contain 2 dark green bags.
# dark green bags contain 2 dark blue bags.
# dark blue bags contain 2 dark violet bags.
# dark violet bags contain no other bags.'''

# rList = data.strip().splitlines()
rList = open('data/07.txt','r').read().strip().splitlines()

# given:
# 1. each row is a rule about the contents of a named bag type
# 2. first two words represent bag type name, then "contain", 
#    then either "no other" or 1+ of (# bag type name) color, then " bags."
# 3. so each rule can define, for a given type of bag, how many of each bag type it can hold (or none)
#
# part 1: how many bag colors can be the *outermost* bag
# part 2: count number of bags a shiny bag contains (recursive)
#
# not going to try making a single regex to split out everything perfect
# my regexfu is insufficient
r = re.compile(r"([^\n ]+ [^ ]+) bags contain (.*[,.]{1})")
rules = {}

searchBag = 'shiny gold'
searchMatchCount = 0

for rule in rList:
    match = r.findall(rule)
    name, containExpression = match[0]
    if containExpression.startswith('no'):
        contains = {}
    else:      
        # convert containExpression first into a key, value list, then a dict
        contains = dict([(" ".join(x.split()[1:3]), x.split()[0]) 
            for x in containExpression.split(', ')])
    rules[name] = contains
    
def checkColor(color):
    matched = False
    for childBag in rules[color]:
        if childBag == searchBag or checkColor(childBag):
            matched = True
    return matched

for color in rules:
    if checkColor(color):
        searchMatchCount += 1
    
def countColor(name):
    cnt = 0
    for x in rules[name]:
        bagCount = int(rules[name][x])
        cnt += bagCount + countColor(x) * bagCount
    return cnt
               
print("Part 1: ", searchMatchCount)
print("Part 2: ", countColor(searchBag))
