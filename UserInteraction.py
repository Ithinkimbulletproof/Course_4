from collections import defaultdict
from CompareVacancies import CompareVacancies


class UserInteraction(CompareVacancies):
    def __init__(self, name_vacancy):
        super().__init__(name_vacancy)
        self.get_vacancy_from_api()
        self.vacancies_list = defaultdict(list)

    def __str__(self):
        self.message = "Vacancy not found" if len(self.all_vacancy) == 0 else self.message
        return (f"Name of vacancy for search: {self.name_vacancy}\n"
                f"Count vacancies: {len(self.all_vacancy)}\n"
                f"Status: {self.message}")

    def make_info(self, top_salary: dict) -> list:
        """
        Created list with vacancies for user.
        :param top_salary: dict with vacancies
        user wants to see
        :return: list with vacancies.
        """
        print(f"Top salary:")

        count = 1
        for top, vacancies in top_salary.items():

            print(f"{count}. Top sallary {top} - count {len(vacancies)}", end='\n')

            for value in vacancies:
                self.vacancies_list[count].extend([{"Name of vacancy": value['name']},
                                                   {"Salary from": value['salary']['from']},
                                                   {"Salary to": value['salary']['to']},
                                                   {"City": value['area']['name']},
                                                   {"URL": f"{value['alternate_url']}\n"}])
            count += 1

    @staticmethod
    def last_info(top_salary: dict, number_of_vacancies: int):
        """
            Get info about top vacancies
            :param number_of_vacancies: number of vacancy from top
            :param top_salary: dict with top vacancies
        """
        print()
        info = []
        for params_vacancy in top_salary[int(number_of_vacancies)]:
            for key, val in params_vacancy.items():
                info.append("{0}: {1}".format(key, val))
        return '\n'.join(info)
