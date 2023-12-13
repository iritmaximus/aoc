from itertools import repeat

def main():
    lines = read_input()

    res_1 = solve(lines)
    print(res_1)
    res_2 = solve_2()
    print(res_2)

    return res_1, res_2

def solve(lines):
    instructions = lines[0]
    max_len = len(instructions)

    tree = construct_tree(lines)
    steps = 0
    i = 0
    node = first_node(lines)
    while True:
        instruction = instructions[i]
        i += 1
        if i > max_len-1:
            i = 0

        if node == "ZZZ":
            return steps

        match instruction:
            case "L":
                node = tree[node].get("left")
            case "R":
                node = tree[node].get("right")
            case "_":
                raise ValueError("Incorrect instruction")

        steps += 1
        print(f"{node} - {i:3} - {steps}")





def construct_tree(lines):
    tree = {}
    for line in lines[2:]:
        id, _, left, right = line.split(" ")
        left = left.strip("(,")
        right = right.strip(")")

        tree[id] = { "left": left, "right": right }
    return tree


def first_node(lines):
    node = lines[2]
    return node[0:3]

def solve_2():
    pass

def read_input(filename: str="input.txt"):
    input = []
    with open(filename) as file:
        lines = file.readlines()

    for line in lines:
        input.append(line.strip())

    return input

if __name__ == "__main__":
    print(main())
