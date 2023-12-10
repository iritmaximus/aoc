
numbers = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "zero": 0
        }


def main():
    result = []

    for line in read_input():
        first_num_L = None
        first_num_R = None

        for i, char in enumerate(line):
            num = find_num_string(i, line)
            
            if char.isnumeric():
                if not first_num_L:
                    first_num_L = char
                first_num_R = char
            if num:
                if not first_num_L:
                    first_num_L = num
                first_num_R = num



        result.append(str(first_num_L) + str(first_num_R))


    sum = 0
    for line in result:
        sum += int(line)

    return sum


def find_num_string(start_i, line):
    for number in numbers.keys():
        if line.startswith(number, start_i):
            return numbers[number]



def read_input():
    filename = "input2.txt"
    input = []
    with open(filename) as file:
        lines = file.readlines()

    for line in lines:
        input.append(line.strip())

    return input


if __name__ == "__main__":
    print(main())
