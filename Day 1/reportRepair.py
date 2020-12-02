filename = "multiplyNum.txt"

with open(filename) as f_obj:
    lines = f_obj.readlines()
    for i in range(len(lines)-1):
        for j in range(i+1, len(lines)):
            if int(lines[j]) == 2020 - int(lines[i]):
                product = int(lines[i]) * int(lines[j])
                print('Part 1: ')
                print(product)

    for i in range(len(lines)-2):
        for j in range(i+1, len(lines)-1):
            for k in range(i, len(lines)-2):
                if int(lines[k]) == (2020 - int(lines[i]) - int(lines[j])):
                    product = int(lines[i]) * int(lines[j]) * int(lines[k])
                    print('Part 2:')
                    print(product)
                    exit()
