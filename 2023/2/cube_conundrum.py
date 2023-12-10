from enum import IntEnum

class Color(IntEnum):
    RED = 1
    BLUE = 2
    GREEN = 3


def sol():
    red_limit = 12
    green_limit = 13
    blue_limit = 14
    limits = [red_limit, green_limit, blue_limit]
    result_1 = []
    result_2 = []

    lines = read_input()
    for line in lines:
        red_max = 0
        green_max = 0
        blue_max = 0

        print(line)
        game_id, rounds = line.split(":")
        game_id = game_id.split(" ")[1]

        for round in rounds.split(";"):
            print(round)
            for cube in round.split(","):
                cube_count, color = cube.strip().split(" ")
                color = cube_color_to_enum(color)
                print(color)
                cube_count = int(cube_count)

                match color:
                    case Color.RED:
                        red_max = max(cube_count, red_max)
                    case Color.GREEN:
                        green_max = max(cube_count, green_max)
                    case Color.BLUE:
                        blue_max = max(cube_count, blue_max)
                    case _:
                        raise ValueError("Incorrect value")
    
        maxes = [red_max, green_max, blue_max]

        # sol 1
        if all_max_inside_limit(limits, maxes):
            result_1.append(int(game_id))

        # sol 2
        product = 1
        for num in maxes:
            product *= num

        result_2.append(product)

    return (sum(result_1), sum(result_2))


def max_inside_limit(limit: int, max: int):
    return limit >= max

def all_max_inside_limit(limits: list[int], maxes: list[int]):
    for i in range(len(limits)):
        if not max_inside_limit(limits[i], maxes[i]):
            return False
    return True


def cube_color_to_enum(color: str):
    if color == "red":
        return Color.RED
    if color == "blue":
        return Color.BLUE
    if color == "green":
        return Color.GREEN
    raise ValueError("None of these")


def read_input(filename: str="input.txt"):
    input = []
    with open(filename) as file:
        lines = file.readlines()

    for line in lines:
        input.append(line.strip())

    return input

if __name__ == "__main__":
    print(sol())
