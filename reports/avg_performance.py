import csv
from tabulate import tabulate
from .base import Report


class AvgPerformanceReport(Report):
    """Отчёт по среднему performance по position."""

    def load_data(self):
        rows = []
        for file in self.files:
            with open(file, encoding="utf-8") as f:
                reader = csv.DictReader(f)
                rows.extend(reader)
        return rows

    def generate(self):
        data = self.load_data()

        groups = {}
        for row in data:
            pos = row["position"]
            perf = float(row["performance"])
            groups.setdefault(pos, []).append(perf)

        result = [
            (position, sum(values) / len(values))
            for position, values in groups.items()
        ]

        # сортировка по убыванию performance
        result.sort(key=lambda x: x[1], reverse=True)

        print(tabulate(result, headers=["position", "avg_performance"], floatfmt=".2f"))
