# passport processing
import re

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

# data = '''eyr:1972 cid:100
# hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

# iyr:2019
# hcl:#602927 eyr:1967 hgt:170cm
# ecl:grn pid:012533040 byr:1946

# hcl:dab227 iyr:2012
# ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

# hgt:59cm ecl:zzz
# eyr:2038 hcl:74454a iyr:2023
# pid:3556412378 byr:2007

# pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
# hcl:#623a2f

# eyr:2029 ecl:blu cid:129 byr:1989
# iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

# hcl:#888785
# hgt:164cm byr:2001 iyr:2015 cid:88
# pid:545766238 ecl:hzl
# eyr:2022

# iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719
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
# p1: count valid passports (based on presence)
# p2: count passports that are both present and have valid values

reqKeys = 'byr iyr eyr hgt hcl ecl pid'.split()

def heightValid(height):
    if height.endswith("cm"):
        try:
            n = int(height[:3])
            if 150 <= n <= 193: return True
        except:
            pass
    if height.endswith("in"):
        try:
            n = int(height[:2])
            if 59 <= n <= 76: return True
        except:
            pass
    return False

validationFuncs = { 'byr':lambda x: 1920 <= int(x)
 <= 2002,
    'iyr':lambda x: 2010 <= int(x) <= 2020,
    'eyr':lambda x: 2020 <= int(x) <= 2030,
    'hgt':lambda x: heightValid(x),
    'hcl':lambda x: len(x) == 7 and x.startswith('#') and all(map(lambda x:x in "abcdef0123456789", list(x[1:]))),
    'ecl':lambda x: x in "amb blu brn gry grn hzl oth".split(),
    'pid':lambda x: len(x) == 9 and x.isdigit(),
    'cid':lambda x: True }

p1valids = []
p2valids = []

# find our field pairs, with care to ungreedily match.
# This could probably be done more concisely; I added the last 
#  bit to this as I wasn't capturing the last field pair.
r = re.compile(r"([^:\n]+?:[^ \n]+)+?[ \n]|(.+:.*)$")

def valid(passport):
    validations = []
    for fields in [field for field in r.findall(passport)]:
        for pair in [x for x in fields if x != '']: # the way this regex works empties are returned
            field, value = pair.split(':')
            isValid = validationFuncs[field](value)
            if not isValid: return False
            validations.append(isValid)
    
    return len(validations) >= 7


for passport in passList:
    if all(map(lambda x:x in passport, reqKeys)): 
        p1valids.append(passport)
        if valid(passport):
            p2valids.append(passport)

# with first test data, results in 2 and 2, with second test data should give 8 and 4.  
print("Part 1: ", len(p1valids))
print("Part 2: ", len(p2valids))