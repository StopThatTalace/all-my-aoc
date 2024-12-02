def get_reports_from_file(filename: str):
    with open(filename, "r") as f:
        return [line.strip().split() for line in f]

def get_total_safe_report(reports: list[list[str]]) -> int:
    return sum(1 for report in reports if is_report_safe(report))


def is_report_safe(report: list[str]) -> bool:

    if report:
        is_ascending = None
        for a, b in list(zip(report, report[1:])):

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

def main():
    print(get_total_safe_report(get_reports_from_file("input.txt")))

if __name__ == "__main__":
    main()