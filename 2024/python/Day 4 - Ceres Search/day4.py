def get_grid_from_file(filename: str):

    with open(filename, "r") as f:
        return [list(line.strip()) for line in f.readlines()]

def count_xmas_part1(grid):
    rows, cols = len(grid), len(grid[0])
    word = "XMAS"
    word_length = len("XMAS")
    directions = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
        (1, 1),
        (-1, -1),
        (1, -1),
        (-1, 1),
    ]

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def check_direction(x, y, dx, dy):
        for i in range(word_length):
            nx, ny = x + i * dx, y + i * dy
            if not is_valid(nx, ny) or grid[nx][ny] != word[i]:
                return False
        return True

    count = 0
    for i in range(rows):
        for j in range(cols):
            for dx, dy in directions:
                if check_direction(i, j, dx, dy):
                    count += 1

    return count


def main():
    print(count_xmas_part1(get_grid_from_file("input.txt")))

if __name__ == "__main__":
    main()