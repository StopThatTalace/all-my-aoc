import re

def extract_all_mul(filename: str):
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

    with open(filename, "r") as f:
        return re.findall(pattern, f.read())

def get_total(all_mul):
    total = 0

    for mul in all_mul:
        total += (int(mul[0])* int(mul[1]))

    return total

def main():
    print(get_total(extract_all_mul("input.txt")))

if __name__ == "__main__":
    main()