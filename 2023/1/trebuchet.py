def main():
    result = []

    for line in read_input():
        first_num_L = None
        first_num_R = None

        for char in line:
            if char.isnumeric():
                if not first_num_L:
                    first_num_L = char
                first_num_R = char

        result.append(str(first_num_L) + str(first_num_R))


    sum = 0
    for line in result:
        sum += int(line)

    return sum


def read_input():
    filename = "input1.txt"
    input = []
    with open(filename) as file:
        lines = file.readlines()

    for line in lines:
        input.append(line.strip())

    return input




if __name__ == "__main__":
    print(main())
