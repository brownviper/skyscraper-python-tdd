def process(sticks):
    side_length = int(sum(sticks) / 4)

    if side_length == 0:
        return 0

    possible_sides = [int(stick_length / side_length) for stick_length in sticks]

    while sum(possible_sides) < 4:
        side_length = side_length - 1
        possible_sides = [stick_length / side_length for stick_length in sticks]

    return side_length
