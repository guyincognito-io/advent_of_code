def read_input(filename):
    with open(filename) as f:
        return f.read()


def parse_reports(data: str) -> list[list[int]]:
    result = []
    for line in data.splitlines():
        result.append([int(n) for n in line.split()])

    return result


def check_report_safety(report: list[int]) -> bool:
    sorted_report = sorted(report)
    reversed_report = sorted(report, reverse=True)

    if not (sorted_report == report or reversed_report == report):
        return False

    diffs = [
        abs(current - ne)
        for current, ne in zip(sorted_report, sorted_report[1:] + [sorted_report[-1]])
    ]

    if all(value in [1, 2, 3] for value in diffs[:-1]):
        return True

    return False


def safety_check(reports: list[list[int]], dampened: bool = False) -> list[bool]:
    result = [False for _ in reports]

    for i in range(len(reports)):
        report_to_check = reports[i]
        report_is_safe = check_report_safety(report_to_check)

        if not dampened or report_is_safe:
            result.append(report_is_safe)
            continue

        for n in range(len(report_to_check)):
            dampened_report = report_to_check[:n] + report_to_check[n + 1 :]
            report_is_safe = check_report_safety(dampened_report)
            if report_is_safe:
                result.append(report_is_safe)
                break

    return result


def main():
    input = read_input("02/input1.txt")
    reports = parse_reports(input)
    safety = safety_check(reports)
    print("Number of reports: ", len(reports))
    print(f"SAFE: {sum(safety)}")
    safety = safety_check(reports, dampened=True)
    print(f"Dampened Reports SAFE: {sum(safety)}")


if __name__ == "__main__":
    main()
