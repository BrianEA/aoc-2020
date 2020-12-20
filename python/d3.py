# day 3: toboggan trajectory
# data lines consistent in length, note some trees have adjacent trees (#)
# the pattern of trees on all lines extends to the right infinitely
# this makes me think of modulus over a sequence...

# data = '''
# ..##.......
# #...#...#..
# .#....#..#.
# ..#.#...#.#
# .#...##..#.
# ..#.##.....
# .#.#.#....#
# .#........#
# #.##...#...
# #...##....#
# .#..#...#.#
# '''
# treeGridList = data.strip().splitlines()
treeGridList = open('data/03.txt','r').read().strip().splitlines()

# given: start position top left corner 
# given 2: need to reach bottom (below bottom-most row on map)
#
# p1: count trees you would encounter for slope right 3, down 1
# p2: check additional slopes, get product of tree counts across slopes

slopes = ((1,1), (3,1), (5,1), (7,1), (1,2))
treeCounts = []
p2product = 1

lineLen = len(treeGridList[0])
for slope in slopes:
    pos = 0
    treeCount = 0
    run = slope[0]
    step = slope[1]
    for line in treeGridList[::step]:
        if line[pos % lineLen] == '#':
            treeCount += 1
        pos += run
    treeCounts.append(treeCount)
    p2product *= treeCount    

print("Part 1: ", treeCounts[1])
print("Part 2: ", p2product)