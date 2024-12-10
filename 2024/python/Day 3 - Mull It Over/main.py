import re

def extract_all_mul_content_part1(filename: str):
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

    with open(filename, "r") as f:
        return re.findall(pattern, f.read())

def get_total_part1(all_mul):
    total = 0

    for mul in all_mul:
        total += (int(mul[0])* int(mul[1]))

    return total

def extract_all_mul_content_part2(filename: str):
    pattern = r"do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\)"

    with open(filename, "r") as f:
        return re.findall(pattern, f.read())


def get_total_part2(all_mul):
    total = 0
    is_enabled = True

    for mul in all_mul:
        if mul == "do()":
            is_enabled = True
        elif mul == "don't()":
            is_enabled = False
        elif mul.startswith("mul") and is_enabled:
            numbers = re.findall(r"\d{1,3}", mul)
            total += int(numbers[0]) * int(numbers[1])

    return total

def main():
    print(get_total_part1(extract_all_mul_content_part1("input.txt")))
    print(get_total_part2(extract_all_mul_content_part2("input.txt")))

if __name__ == "__main__":
    main()