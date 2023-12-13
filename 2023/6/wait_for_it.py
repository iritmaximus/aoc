def main():
    lines = read_input()
    for line in lines:
        print(line)

    
    # times to list
    times = filter(None, lines[0].split(":")[1].strip().split(" "))
    times_2 = int("".join(times))
 
    times = [int(x.strip()) for x in times]
    print(times)

    # distance to list
    record_distances = filter(None, lines[1].split(":")[1].strip().split(" "))
    record_distance_2 = int("".join(record_distances))
    record_distances = [int(x.strip()) for x in record_distances]
    print(record_distances)
    print()

    res_1 = solve(times, record_distances)
    print(res_1)
    res_2 = solve_2(times_2, record_distance_2)
    print(res_2)

    return res_1, res_2

def solve_2(time, record_distance):
    count = 0
    for i in range(time):
        speed = i
        remaining_time = time - i
        if remaining_time == 0:
            continue

        if speed*remaining_time > record_distance:
            count += 1

    return count

def solve(times, record_distances):
    result = []
    for time, record_distance in zip(times, record_distances):
        distances = []
        for i in range(time):
            speed = i
            remaining_time = time - i
            if remaining_time == 0:
                continue

            #print(speed*remaining_time, speed*remaining_time > record_distance)
            if speed*remaining_time > record_distance:
                distances.append(i)

        print(distances, len(distances))
        result.append(len(distances))

    product = 1
    for num in result:
        product *= num

    return product


def read_input(filename: str="input.txt"):
    input = []
    with open(filename) as file:
        lines = file.readlines()

    for line in lines:
        input.append(line.strip())

    return input

if __name__ == "__main__":
    print(main())
