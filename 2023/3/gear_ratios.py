def sol_1():
    lines = read_input()
    #lines = read_input("example_input.txt")

    max_x = len(lines[0])
    max_y = len(lines)
    print(max_x, max_y)

    result_1 = []


    for j, line in enumerate(lines):
        line = line.strip()
        print(lines[j if j-1<0 else j-1])
        print(line)
        print(lines[j if j+1>(max_y-1) else j+1])

        num = ""
        is_partnumber = False
        for i, char in enumerate(line):
            if char.isnumeric():
                number_cords = (i, j)
                #print_cluster_around_cords(number_cords, lines, max_x, max_y)
                if not is_partnumber:
                    if check_around_cords(number_cords, lines, max_x, max_y):
                        is_partnumber = True
                num += char
            else:
                if num:
                    print(f"num: {num:3} - {is_partnumber}")

                if num and is_partnumber:
                    result_1.append(int(num))
                num = ""
                is_partnumber = False

    return sum(result_1)


def check_around_cords(cords, lines, max_x, max_y):
    x, y = cords
    values = [1, 0, -1]
    #print("starting new round")

    for y_value in values:
        if y-y_value > max_y - 1 or y-y_value < 0:
            continue

        for x_value in values:
            if x-x_value > max_x - 1 or x-x_value < 0:
                continue

            char = lines[y - y_value][x - x_value]
            #print(f"({x-x_value},{y-y_value}): {char}")
            if not char == "." and not char.isnumeric():
                return True


def print_cluster_around_cords(cords, lines, max_x, max_y):
    x, y = cords
    values = [1, 0, -1]
    test_cluster = []

    for y_value in values:
        if y-y_value > max_y - 1 or y-y_value < 0:
            continue

        test_cluster_item = []
        for x_value in values:
            if x-x_value > max_x - 1 or x-x_value < 0:
                continue

            test_cluster_item.append(lines[y - y_value][x - x_value])
        test_cluster.append(test_cluster_item)

    for line in test_cluster:
        print(line)


def print_input(lines):
    for line in lines:
        print(line)

def read_input(filename: str="input.txt"):
    input = []
    with open(filename) as file:
        lines = file.readlines()

    for line in lines:
        input.append(line.strip())

    return input

if __name__ == "__main__":
    print(sol_1())
