filename = 'tobogganTrajectory.txt'


def findSlope(right, down):
    with open(filename) as f_obj:
        lines = f_obj.readlines()
        index = 0
        vertical = 1
        tree = 0
        for line in lines:
            if vertical % down == 0 and line[index] == '#':
                tree += 1
            index = (index + right) % (len(line)-1)
            vertical += 1
        return(tree)


print('Part 1: ' + str(findSlope(3, 1)) + '\n')

print('Part 2: ' + str(findSlope(1, 1) * findSlope(3, 1) * findSlope(5, 1) *
      findSlope(7, 1) * findSlope(1, 2)))
