
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

class LineStringNums:
    def __init__(self, line):
        self.line = line
        self.line_nums = self.transform_str_ints_to_ints(line)
        self.num_indexes_list = self.num_indexes()

    def transform_str_ints_to_ints(self, line):
        list = []
        num_strings = numbers.keys()
        for num_string in num_strings:
            index = line.find(num_string)
            if line.find(num_string) != -1:
                list.append({"value": numbers[num_string], "index": index})
        return list if list else None

    def num_indexes(self) -> list[int]:
        list = []
        if not self.line_nums:
            return []
        for line_dict in self.line_nums:
            list.append(line_dict.get("index"))
        if list:
            return sorted(list)
        return []

    def __str__(self):
        return f"{self.line}: {self.line_nums}"


def main():
    raw_lines = read_input()
    for line in raw_lines:
        line_nums = LineStringNums(line)
        print(line_nums, line)

        for char in line:
            



def get_sum_from_int(list):
    result = []

    for line in list:
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
    filename = "input2.txt"
    input = []
    with open(filename) as file:
        lines = file.readlines()

    for line in lines:
        input.append(line.strip())

    return input


if __name__ == "__main__":
    print(main())
