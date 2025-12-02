import argparse
from reports.avg_performance import AvgPerformanceReport


REPORTS = {
    "avg_performance": AvgPerformanceReport,
}


def parse_args():
    parser = argparse.ArgumentParser(description="Report generator")

    parser.add_argument(
        "--files",
        nargs="+",
        required=True,
        help="Входные CSV-файлы"
    )

    parser.add_argument(
        "--report",
        required=True,
        choices=REPORTS.keys(),
        help="Название отчёта"
    )

    return parser.parse_args()


def main():
    args = parse_args()

    report_class = REPORTS[args.report]
    report = report_class(args.files)
    report.generate()


if __name__ == "__main__":
    main()
