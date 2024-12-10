def get_reports_from_file(filename: str):
    with open(filename, "r") as f:
        return [line.strip().split() for line in f]

def get_total_safe_report_part1(reports: list[list[str]]) -> int:
    return sum(1 for report in reports if is_report_safe_part1(report))

def get_total_safe_report_part2(reports: list[list[str]]) -> int:
    return sum(1 for report in reports if is_report_safe_part2(report))


def is_report_safe_part1(report: list[str]) -> bool:
    if not report:
        return False

    is_ascending = None
    for a, b in zip(report, report[1:]):
        diff = int(b) - int(a)

        if not (-3 <= diff <= -1 or 1 <= diff <= 3):
            return False

        if diff > 0:
            if is_ascending is False:
                return False
            is_ascending = True
        elif diff < 0:
            if is_ascending is True:
                return False
            is_ascending = False

    return True

def is_report_safe_part2(report: list[str]) -> bool:
    if is_report_safe_part1(report):
        return True

    for i in range(len(report)):
        """
        1. get all elements from report from the startup to i (no including it)
        2. add it up with all element from element starting from i to the end (no including it)
        result : create a list without this element.
        """
        modified_report = report[:i] + report[i + 1:]
        if is_report_safe_part1(modified_report):
            return True

    return False


def main():
    print(get_total_safe_report_part1(get_reports_from_file("input.txt")))
    print(get_total_safe_report_part2(get_reports_from_file("input.txt")))



if __name__ == "__main__":
    main()
