
def main():
    lines = read_input()

    seeds = lines[0].split(" ")
    seeds = [int(seed) for seed in seeds[1:]]
    lowest = float("inf")

    res_1 = solve(lines, seeds)
    print(res_1)


    maps = [
            generate_map(lines, "seed-to-soil"), 
            generate_map(lines, "soil-to-fertilizer"), 
            generate_map(lines, "fertilizer-to-water"),
            generate_map(lines, "water-to-light"),
            generate_map(lines, "light-to-temperature"),
            generate_map(lines, "temperature-to-humidity"),
            generate_map(lines, "humidity-to-location"),
            ]

    results = []
    for i in range(0, len(seeds), 2):
        for x in range(seeds[i+1]):
            seed =  solve_2(lines, seeds[i] + x)
            #seed =  solve_2_maps(maps, seeds[i] + x)
            lowest = seed if seed < lowest else lowest
            print(f"{i}/{len(seeds)} - {(x/seeds[i+1])*100:.2f}%: {x} --- {lowest} - {results}")
        results.append(lowest)


    res_2 = lowest
    print(res_2)

    return res_1, res_2


def solve_2_maps(maps, seed):
    for map in maps:
        transformed_seed = solve_2_map(map, seed)
        if transformed_seed:
            seed = transformed_seed
    return seed


def solve_2_map(map, seed):
    for line in map:
        if in_range(seed, line[1], line[2]):
            transfromed_seed = transform_seed_to_dest(seed, line[1], line[0])
            print("seed", seed, "in range", line[0], "-", line[0]+line[2], "=", transfromed_seed)
            return transfromed_seed


def solve_2(lines, seed):
    transformed_seed = float("inf")


    for line in lines[1:]:
        if not line.strip() or line[-1] == ":":
            if transformed_seed == float("inf"):
                transformed_seed = seed

            seed = transformed_seed
            transformed_seed = float("inf")
            continue

        if transformed_seed != float("inf"):
            continue

        values = line.split(" ")
        destination_start_range = int(values[0])
        source_start_range = int(values[1])
        count = int(values[2])

        if in_range(seed, source_start_range, count):
            if transformed_seed == float("inf"):
                transformed_num = transform_seed_to_dest(seed, source_start_range, destination_start_range)
                transformed_seed = transformed_num

    if transformed_seed == float("inf"):
        transformed_seed = seed

    seed = transformed_seed
    return seed

def generate_map(lines, map_str):
    is_map = False
    some_map = []
    for line in lines:
        #print("line", line)

        if map_str in line:
            is_map = True
            continue

        if not is_map or not line.strip() or line[-1] == ":":
            continue

        values = line.split(" ")
        destination_start_range = int(values[0])
        source_start_range = int(values[1])
        count = int(values[2])
        some_map.append([destination_start_range, source_start_range, count])

        if not line.strip():
            break

    return some_map

def solve(lines, seeds):
    transformed_seeds = [0] * len(seeds)
    for line in lines[1:]:
        #print(line)

        if not line.strip() or line[-1] == ":":
            #print(seeds)
            for i, seed in enumerate(seeds):
                if transformed_seeds[i] == 0:
                    transformed_seeds[i] = seeds[i]

            seeds = transformed_seeds
            transformed_seeds = [0] * len(seeds)
            continue

        values = line.split(" ")
        destination_start_range = int(values[0])
        source_start_range = int(values[1])
        count = int(values[2])

        for i, seed in enumerate(seeds):
            if in_range(seed, source_start_range, count):
                if transformed_seeds[i] == 0:
                    transformed_num = transform_seed_to_dest(seed, source_start_range, destination_start_range)
                    transformed_seeds[i] = transformed_num
                    #print("seed", seed, "in range", source_start_range, "-", source_start_range+count, "=", transformed_num)

    for i, seed in enumerate(seeds):
        if transformed_seeds[i] == 0:
            transformed_seeds[i] = seeds[i]
    seeds = transformed_seeds

    print(seeds)
    return min(seeds)


def in_range(seed_num, ssr, count):
    if seed_num >= ssr and ssr+count >= seed_num:
        return True
    return False

def transform_seed_to_dest(seed_num, ssr, dsr):
    return dsr + (seed_num - ssr)

def all_in_range(start_num, range_num):
    result = []
    for x in range(range_num):
        result.append(start_num + x)
    return result


def read_input(filename: str="input.txt"):
    input = []
    with open(filename) as file:
        lines = file.readlines()

    for line in lines:
        input.append(line.strip())

    return input

if __name__ == "__main__":
    print(main())
