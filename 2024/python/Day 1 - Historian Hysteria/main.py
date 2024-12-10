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

def get_similarity(distance_1: list[int], distance_2: list[int]):
    total_similarity = 0

    for number in distance_1:
        total_similarity += number * distance_2.count(number)

    return total_similarity


def main():
    distance_1, distance_2 = get_lists_from_file("input.txt")
    print(get_total_distance(distance_1, distance_2))
    print(get_similarity(distance_1, distance_2))




if __name__ == "__main__":
    main()