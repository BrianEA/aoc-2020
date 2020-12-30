# Day 9: Encoding Error
import itertools
import sys

# data = '''35
# 20
# 15
# 25
# 47
# 40
# 62
# 55
# 65
# 95
# 102
# 117
# 150
# 182
# 127
# 219
# 299
# 277
# 309
# 576
# ''' 

# nums = [int(x) for x in data.strip().splitlines()]
nums = [int(x) for x in open('data/09.txt','r').read().strip().splitlines()]

# after 25 (5 in test data) number preamble
# each valid number is the sum of 2 two of the previous 25 numbers
# part 1: search for first invalid number
# part 2: find a contiguous set of inputs for which their sum is the invalid number 
#  from part 1.

preamble = 1
preamble_length = 25
invalidNum = -1
d = {}

def calculate(start, end):
    global preamble
    if preamble:
        for i in range(start, end+1):
            d[i] = [nums[i]+nums[j] for j in range(start,end+1)]
        preamble = 0
    else:
        del d[start-1]
        d[end] = [nums[end]+nums[j] for j in range(start,end+1)]

for x in range(preamble_length, len(nums)):
    calculate(x-preamble_length, x-1)
    if nums[x] not in list(itertools.chain(*d.values())):
        invalidNum = nums[x]
        print(invalidNum, ' not in sums')
        break

#print(list(itertools.chain(*d.values())))

# after each unsuccessful search, increase size of window
# window cannot be larger than len(nums)
windowSize = 2
while windowSize < len(nums)+1:
    for idx in range(len(nums)+1-windowSize):
        if sum(nums[idx:idx+windowSize]) == invalidNum:
            solveList = list(nums[idx:idx+windowSize])
            solveList.sort()          
            print("Final window size: ", windowSize)
            print("Part 2: ", solveList[0]+solveList[windowSize-1])
            sys.exit(0)
    windowSize += 1
