#testdata = '''1721
979
366
299
675
1456
#''' 

lines = open('data/01.txt','r').readlines()

nums = [int(x) for x in lines]
nums.sort()

def getMatches():
    for i in nums:
        for j in nums:
            for k in nums:
                if i+j == 2020:
                    return (i,j)


x,y = getMatches()
print('Part 1: ', x*y)

def getMatches2():
    for i in nums:
        for j in nums:
            for k in nums:
                if i+j+k == 2020:
                    return (i,j,k)

x,y,z = getMatches2()
print('Part 2: ', x*y*z)
