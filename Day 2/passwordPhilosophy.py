filename = 'passwordPhilosophy.txt'

with open(filename) as f_obj:
    lines = f_obj.readlines()
    good = 0
    valid = 0
    for line in lines:
        conditions = line.split()
        limits = list(map(int, conditions[0].split('-')))
        alphabet = conditions[1].strip(':')
        password = conditions[2]
        count = 0
        for index, letter in enumerate(password):
            if letter == alphabet:
                count += 1
                if index+1 == limits[0] and password[limits[1]-1] != alphabet:
                    good += 1
                elif index+1 == limits[1] and password[limits[0]-1] != alphabet:
                    good += 1

        if count >= limits[0] and count <= limits[1]:
            valid += 1

    print('Part 1: ' + str(valid) +
          ' password(s) of the given list are valid according to the policy.')
    print('\nPart 2: ' + str(good) +
          ' password(s) of the given list are valid according to the policy.')
