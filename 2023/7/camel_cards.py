from enum import IntEnum

class PictureCard(IntEnum):
    A = 14
    K = 13
    Q = 12
    J = 1
    T = 10

class HandType(IntEnum):
    FIVE = 7
    FOUR = 6
    FULLHOUSE = 5
    THREE = 4
    TWO = 3
    ONE = 2
    HIGH = 1

def main():
    lines = read_input()

    print("PART 1:")
    res_1 = solve(lines, False)
    print("PART 2:")
    res_2 = solve(lines, True)

    return (res_1, res_2)


def solve(lines, second_part: bool):
    hands = []
    for line in lines:
        hand, bid = line.split(" ")
        hands.append({"hand": hand, "bid": int(bid), "card_count": get_card_count(hand, second_part)})

    sorted_hands = sorted(hands, key=lambda hand: hand_value(hand), reverse=False)
    result = 0
    for i, hand in enumerate(sorted_hands):
        result += hand.get("bid") * (i + 1)
        print(hand, i+1, "=", hand.get("bid") * (i + 1))

    return result



def hand_type(card_count):
    # len(card_count)
    # 1: five-of-a-kind
    # 2: four-of-a-kind, full house
    # 3: Three-of-a-kind, two two-of-a-kind
    # 4: two-of-a-kind
    # 5: high card

    match len(card_count):
        case 1:
            return HandType.FIVE
        case 2:
            card_count_values = card_count.values()
            # is it four-of-a-kind or fullhouse
            if 4 in card_count_values:
                return HandType.FOUR
            return HandType.FULLHOUSE

        case 3:
            card_count_values = card_count.values()
            if 3 in card_count_values:
                return HandType.THREE
            return HandType.TWO

        case 4:
            return HandType.ONE

        case 5:
            return HandType.HIGH

        case _:
            raise ValueError("Hand type not matched")




def get_card_count(hand, second_part):
    card_count = {}
    for card in hand:
        if card_count.get(card):
            card_count[card] += 1
        else:
            card_count[card] = 1

    if second_part:
        jokers = card_count.get("J")
        if jokers:
            card_count["J"] = 0
            max_value = max(card_count.values())
            for card_count_key in card_count:
                if card_count[card_count_key] == max_value and card_count_key != "J":
                    card_count[card_count_key] += jokers
            del card_count["J"]
            if len(card_count) == 0:
                card_count["A"] = 5

    return card_count


def hand_value(hand):
    card_count = hand.get("card_count")
    hand = hand.get("hand")
    hand_type_value = hand_type(card_count)

    hand_card_value = []
    for card in hand:
        if card.isnumeric():
            hand_card_value.append(int(card))
        else:
            #A = 14
            #K = 13
            #Q = 12
            #J = 11
            #T = 10
            match card:
                case "A":
                    hand_card_value.append(PictureCard.A)
                case "K":
                    hand_card_value.append(PictureCard.K)
                case "Q":
                    hand_card_value.append(PictureCard.Q)
                case "J":
                    hand_card_value.append(PictureCard.J)
                case "T":
                    hand_card_value.append(PictureCard.T)
                case _:
                    raise ValueError("No picture card matched")

    return [hand_type_value, hand_card_value]


def read_input(filename: str="input.txt"):
    input = []
    with open(filename) as file:
        lines = file.readlines()

    for line in lines:
        input.append(line.strip())

    return input

if __name__ == "__main__":
    print(main())
