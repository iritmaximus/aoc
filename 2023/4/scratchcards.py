def sol_1():
    lines = read_input()
    #lines = read_input("example_input.txt")
    sum = 0
    card_count = inin_card_count(len(lines))

    for line in lines:
        #print(line)

        winning_nums, elf_nums = line.split("|")
        game_id, winning_nums = winning_nums.split(":")
        game_id = int(game_id[4:].strip())
        
        winning_nums = list(filter(None, winning_nums.split(" ")))
        elf_nums = list(filter(None, elf_nums.split(" ")))

        # count how many matching numbers there are on the current card
        count = 0
        for num in elf_nums:
            if num in winning_nums:
                count += 1

        # count the new winning cards
        for num in range(1, count+1):
            # add to the "forward card" the amount of times it is won
            card_count[game_id+num] += card_count[game_id]
        print(game_id, card_count, count)

        if count > 0:
            sum += 2**(count - 1)

    card_count_num = 0
    for game_id in card_count:
        card_count_num += card_count[game_id]

    print(card_count)
    print()
    return (sum, card_count_num)


def inin_card_count(lines_len):
    card_count = {}
    for i in range(1, lines_len+1):
        card_count[i] = 1

    return card_count

def read_input(filename: str="input.txt"):
    input = []
    with open(filename) as file:
        lines = file.readlines()

    for line in lines:
        input.append(line.strip())

    return input

if __name__ == "__main__":
    print(sol_1())
