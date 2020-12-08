def readFile():
    filename = 'testCase.txt'
    #filename = 'handyHaversacks.txt'
    with open(filename) as file:
        lines = file.readlines()
        return lines


def partOne():
    colors = []
    bag = 'shiny gold'
    for line in readFile():
        line = (line.replace('bags', '').replace('bag', '')
                .replace('.\n', '').strip().split('contain'))
        if bag in line[1]:
            colors.append(line[0].strip())
    for color in colors:
        for line in readFile():
            line = line.replace('bags', '').replace('bag', '').split('contain')
            if color in line[1]:
                colors.append(line[0].strip())
    return len(set(colors))


print('Part 1: ', partOne())
