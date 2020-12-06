def read_file():
    filename = 'customCustoms.txt'
    # filename = 'testCase.txt'
    with open(filename) as file:
        lines = file.read().split('\n\n')
    return lines


def partOne():
    count = 0
    for line in read_file():
        survey = set(line.replace('\n', ''))
        count += len(survey)
    return count


def partTwo():
    read_file()
    count = 0
    for line in read_file():
        survey = set(line.replace('\n', ''))
        answer = line.split()
        count += sum(all(i in j for j in answer) for i in survey)
    return count


print('Part 1: ', partOne())
print('Part 2: ', partTwo())
