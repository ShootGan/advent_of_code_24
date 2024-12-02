def read_data(file_path):
    with open(file_path, 'r') as file:
        reports_lists = [line.strip().split() for line in file]
    return reports_lists

def check_order(report: list) -> bool:
    if report == sorted(report) or report == sorted(report, reverse=True):
        return True
    return False

def  check_elements_differ(report: list) -> bool:
    for index, value in enumerate(report[:-1]):
        if abs(report[index+1] - value) > 3:
            return False
    return True

def validate_report(report: list) -> bool:
    report = list(map(int, report))
    if not check_order(report):
        return False
    if len(set(report)) != len(report):
        return False
    if not check_elements_differ(report):
        return False
    return True

def count_valid_reports_with_tolerance(reports: list) -> int:
    valid_reports = 0 
    for report in reports:
        if validate_report(report):
            valid_reports += 1
            continue
        for i in range(len(report)):
            if validate_report(report[:i] + report[i+1:]):
                valid_reports += 1
                break
    return valid_reports

def count_valid_reports(reports: list) -> int:
    valid_reports = 0
    for report in reports:
        if validate_report(report):
            valid_reports += 1
    return valid_reports

if __name__ == "__main__":
    reports_list = read_data('day2/input.txt')
    valid_reports_number = count_valid_reports(reports_list)
    print(f'Number of valid reports: {valid_reports_number}')
    valid_reports_with_margin = count_valid_reports_with_tolerance(reports_list)
    print(f'Number of valid reports with margin: {valid_reports_with_margin}')
