# binary boarding
import numpy as np

# data is consistent pattern of len 10 strings
#data = '''BBFFBBFRLL''' # row 44, seat ID 357

#passList = data.strip().splitlines()

passList = open('data/05.txt','r').read().strip().splitlines()

# given:
# each row is a seat designation, determined by string of characters
# F=front, B=back, L=left, R=right
# first 7 characters determine row
# last 3 determine column
# seat id = row * 8 + column
#
# p1: what is highest seat ID on a boarding pass,
# essentially a binary search front to back, then left to right
#
# p2: find 1 seat gap not in either end, and return its id

# zero filled array with x,y dimensions
a = np.zeros((8,128))
taken = []

def boardReduce(chars, size):
    s = 0
    e = size
    
    for x in chars:
        if x == 'F' or x == 'L':
            e = s + (e-s) // 2
        if x == 'B' or x == 'R':
            s = s + (e-s) // 2
        
    return s

def getSeatId(bp):
    row = boardReduce(list(bp[:7]), 128)
    col = boardReduce(list(bp[-3:]), 8)
    seatId = row * 8 + col
    taken.append(seatId)
    a[col,row] = 1
    return seatId
  
print("Part 1: ", max(map(getSeatId, passList)))

# need to find the numpy elegant way of doing this
for row in range(128):
    for col in range(8):
        seatId = row * 8 + col
        if a[col, row] != 1 and seatId-1 in taken and seatId+1 in taken:
            print("Part 2: ", seatId)         
            break