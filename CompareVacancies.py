from GetVacancies import GetVacancies
from collections import defaultdict


class CompareVacancies(GetVacancies):
    def __init__(self, name_vacancy: str):
        super().__init__(name_vacancy)
        self.sort_salary: dict = defaultdict(list)
        self.top_salary: dict = defaultdict(list)

    def sorted_salary(self, list_all: list, salary: int, city: str) -> dict:
        """
           Generate dict with necessary salary
           with vacancies' list
        """

        for vacancy in list_all:
            if vacancy["salary"] is not None and vacancy["salary"]["from"] is not None:
                if vacancy["area"]["name"] == city:
                    if vacancy["salary"]['from'] >= salary and vacancy["salary"]['from'] is not None:
                        self.sort_salary[vacancy["salary"]['from']].append(vacancy)
        return self.sort_salary

    def get_top_vacancies(self, sort_salary) -> list:
        """
        Get top vacancies.
        :return: list with vacancies.
        """

        for top, vacancy in sort_salary.items():
            for value in vacancy:
                if value["salary"] is not None and value["salary"]["to"] is not None:
                    self.top_salary[value["salary"]["to"]].extend(vacancy)

        self.top_salary = dict(sorted(self.top_salary.items(), reverse=True))

        if len(self.top_salary) < 1:
            self.message = "Vacancy not found"
            return self.message

        return self.top_salary

