# passport processing
import re
import itertools

# data = '''ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
# byr:1937 iyr:2017 cid:147 hgt:183cm

# iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
# hcl:#cfa07d byr:1929

# hcl:#ae17e1 iyr:2013
# eyr:2024
# ecl:brn pid:760753108 byr:1931
# hgt:179cm

# hcl:#cfa07d eyr:2025 pid:166559648
# iyr:2011 ecl:brn hgt:59in
# '''
# passList = data.strip().split('\n\n')

passList = open('data/04.txt','r').read().strip().split('\n\n')

# given:
# k/v pairs separated by spaces or newlines.
# blank lines separate passports
# expected fields: byr iyr eyr hgt hcl ecl pid cid
# required fields: all but cid
# valid passports have all required fields
#
# p1: count valid passports

validKeys= 'byr iyr eyr hgt hcl ecl pid cid'.split()  #might need in p2
reqKeys = 'byr iyr eyr hgt hcl ecl pid'.split()

p1valids = []
p2valids = []
for passport in passList:
    if all(map(lambda x:x in passport, reqKeys)): 
        p1valids.append(passport)

print("Part 1: ", len(p1valids))
print("Part 2: ", len(p2valids))