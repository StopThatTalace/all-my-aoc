def get_lists_from_file(filename: str):
    distance_1 = []
    distance_2 = []

    with open(filename, "r") as f:
        for line in f:
            distances = line.strip().split("   ")
            distance_1.append(int(distances[0]))
            distance_2.append(int(distances[1]))

    return distance_1, distance_2

def get_total_distance(distance_1: list[int], distance_2: list[int]) -> int:
    total_distance = 0

    sorted_list_1 = sorted(distance_1)
    sorted_list_2 = sorted(distance_2)

    for i in range(len(sorted_list_1)):
        total_distance += int(str((sorted_list_1[i] - sorted_list_2[i])).strip("-"))

    return total_distance


def main():
    distance_1, distance_2 = get_lists_from_file("input.txt")
    total_distance = get_total_distance(distance_1, distance_2)
    print(total_distance)

if __name__ == "__main__":
    main()