Этот проект позволяет формировать различные аналитические отчёты по CSV-файлам сотрудников.
В текущей версии реализован отчёт по среднему показателю performance в разрезе должностей.
Архитектура скрипта поддерживает лёгкое добавление новых отчётов.


Требования

Python 3.10+

Поддержка UTF-8 CSV-файлов

 
 Как добавить новый отчёт

1️. Создайте новый файл в reports/:
Например: tech_skills_report.py

2. Унаследуйтесь от класса Report:

from .base import Report

class TechSkillsReport(Report):
    def generate(self):
        ...


3️. Добавьте отчёт в REPORTS в main.py

from reports.tech_skills_report import TechSkillsReport

REPORTS = {
    "avg_performance": AvgPerformanceReport,
    "tech_skills": TechSkillsReport,
}


Теперь можно вызвать:

python main.py --files data.csv --report tech_skills
