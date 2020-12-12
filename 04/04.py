
import re

# Part One
# Functions to Check Passport Fields

def checkPassport(passport):
    for f in fields:
        if f not in passport:
            return False
    return True

# Main code for Part One

with open('data.txt') as file:
    data = file.readlines()
    data = [line.strip() for line in data]

fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
validPassports = []
passportToCheck = ''

for line in data:
    if line != '':
        passportToCheck += ' ' + line
    else:
        if checkPassport(passportToCheck):
            validPassports.append(passportToCheck)
        passportToCheck = ''
if checkPassport(passportToCheck):
    validPassports.append(passportToCheck)

print(len(validPassports))

# Part Two
#Functions to Check Passport Attributes

def check_byr(byr):
    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    if int(byr) >= 1920 and int(byr) <= 2002:
        return True
    return False

def check_iyr(iyr):
    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    if int(iyr) >= 2010 and int(iyr) <= 2020:
        return True
    return False

def check_eyr(eyr):
    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    if int(eyr) >= 2020 and int(eyr) <= 2030:
        #print(eyr)
        return True
    return False

def check_hgt(hgt):
    # hgt (Height) - a number followed by either cm or in:
    # If cm, the number must be at least 150 and at most 193.
    # If in, the number must be at least 59 and at most 76.
    unit = hgt[-2:]
    #print(unit)
    if unit == 'cm':
        height = int(hgt[:-2])
        #print(height)
        if height >= 150 and height <= 193:
            return True
    elif unit == 'in':
        height = int(hgt[:-2])
        #print(height)
        if height >= 59 and height <= 76:
            return True

    return False

def check_hcl(hcl):
    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    #print(hcl)
    if hcl[:1] == '#':
        #print(hcl)
        if bool(re.match(r"[0-9a-f]{6}",hcl[1:])):
            #print(hcl)
            return True
    return False

def check_ecl(ecl):
    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    for c in colors:
        if ecl == c:
            #print(ecl)
            return True
    return False

def check_pid(pid):
    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    if bool(re.match(r'^\d{9}$',pid)):
        #print(pid)
        return True
    return False

def check_passport_attributes(passport):
    cleanPassport = passport.strip()
    pairs = cleanPassport.split()
    passportData = {}

    for p in pairs:
        keyval = p.split(":")
        key = keyval[0]
        val = keyval[1]
        passportData[key] = val

    #print(passportData)

    if not check_byr(passportData['byr']):
        return False

    if not check_iyr(passportData['iyr']):
        return False

    if not check_eyr(passportData['eyr']):
        return False

    if not check_hgt(passportData['hgt']):
        return False

    if not check_hcl(passportData['hcl']):
        return False

    if not check_ecl(passportData['ecl']):
        return False

    if not check_pid(passportData['pid']):
        return False

    return True

verifiedPassports = []

for passport in validPassports:
    if check_passport_attributes(passport):
        verifiedPassports.append(passport)

print(len(verifiedPassports))