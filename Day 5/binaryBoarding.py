filename = 'BinaryBoarding.txt'

with open(filename) as file:
    lines = file.readlines()
    seats = []
    for line in lines:
        line = (line.replace('F', '0').replace('B', '1')
                .replace('R', '1').replace('L', '0'))
        row = int(line[:7], 2)
        column = int(line[7:], 2)
        seat = row * 8 + column
        seats.append(seat)
    print('Part 1: ', max(seats))

    for seat_id in seats:
        if (seat_id + 1 not in seats) and (seat_id +2 in seats):
            print('Part 2: ', seat_id + 1)
