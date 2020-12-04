import re


def readText():
    filename = 'passportProcessing.txt'
    with open(filename) as f_obj:
        lines = f_obj.read()
    info = lines.strip().split('\n\n')
    details = []
    for each in info:
        details.append(each.replace('\n', ':').
                       replace(' ', ':').strip().split(':'))
    return details


def passportVerificationSimple():
    valid = 0
    for each in readText():
        if len(each) == 16:

            valid += 1
        elif len(each) == 14 and 'cid' not in each:
            valid += 1
    return valid


def passportVerificationStrict():
    eyes = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    verified = 0

    for each in readText():
        valid = 0
        if len(each) == 16 or len(each) == 14:
            if len(each) == 14 and 'cid' in each:
                each[0] = 'Ignore'

            for i in range(0, len(each)-1, 2):

                if each[i] == 'byr':
                    if (len(each[i+1]) == 4 and int(each[i+1]) >= 1920
                       and int(each[i+1]) <= 2002):
                        valid += 1

                elif each[i] == 'iyr':
                    if (len(each[i+1]) == 4 and int(each[i+1]) >= 2010
                       and int(each[i+1]) <= 2020):
                        valid += 1

                elif each[i] == 'eyr':
                    if (len(each[i+1]) == 4 and int(each[i+1]) >= 2020
                       and int(each[i+1]) <= 2030):
                        valid += 1

                elif each[i] == 'hgt':
                    if ('cm' in each[i+1]):
                        height = int(each[i+1].strip('cm'))
                        if height >= 150 and height <= 193:
                            valid += 1

                    elif ('in' in each[i+1]):
                        height = int(each[i+1].strip('in'))
                        if height >= 59 and height <= 76:
                            valid += 1

                elif each[i] == 'hcl':

                    hair = each[i+1]
                    if hair[0] == '#' and len(hair) == 7:
                        hair = hair.strip('#')
                        color = re.compile(r'[a-fA-F0-9]')
                        if len(color.findall(hair)) == 6:
                            valid += 1

                elif (each[i] == 'ecl' and each[i+1] in eyes):

                    valid += 1

                elif (each[i] == 'pid' and len(each[i+1]) == 9):
                    if (each[i+1]).isnumeric() is True:
                        valid += 1

            if valid == 7:
                verified += 1

    return verified


print('Part 1: ', passportVerificationSimple())
print('Part 2: ', passportVerificationStrict())
