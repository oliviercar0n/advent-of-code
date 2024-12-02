with open("day-02.txt", "r") as f:
    input_data = f.read().strip().split("\n")


def is_report_safe(report):
    diffs = [report[i + 1] - report[i] for i in range(len(report) - 1)]

    diff_check = all(1 <= abs(x) <= 3 for x in diffs)
    all_increasing = all(x > 0 for x in diffs)
    all_decreasing = all(x < 0 for x in diffs)

    return diff_check and (all_increasing or all_decreasing)


# Part 1

acc = 0
for line in input_data:
    report = [int(x) for x in line.split(" ")]
    if is_report_safe(report):
        acc += 1

print(acc)

# Part 2

acc = 0
for line in input_data:
    report = [int(x) for x in line.split(" ")]
    if is_report_safe(report):
        acc += 1
    else:
        for x in range(len(report)):
            nr = report.copy()
            nr.pop(x)
            if is_report_safe(nr):
                acc += 1
                break

print(acc)
