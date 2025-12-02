from reports.avg_performance import AvgPerformanceReport
import tempfile


def test_avg_report_basic():
    # создаём временный файл с CSV
    csv_data = """name,position,completed_tasks,performance,skills,team,experience_years
A,Dev,10,1.0,Python,Alpha,2
B,Dev,20,3.0,Python,Beta,3
C,QA,5,2.0,Tests,Alpha,1
"""
    with tempfile.NamedTemporaryFile("w", delete=False, suffix=".csv") as f:
        f.write(csv_data)
        filename = f.name

    report = AvgPerformanceReport([filename])
    data = report.load_data()

    assert len(data) == 3

    # проверяем правильность среднего
    groups = {"Dev": [1.0, 3.0], "QA": [2.0]}
    result = {}
    for row in data:
        pos = row["position"]
        perf = float(row["performance"])
        result.setdefault(pos, []).append(perf)

    assert sum(result["Dev"]) / len(result["Dev"]) == 2.0
    assert sum(result["QA"]) / len(result["QA"]) == 2.0
