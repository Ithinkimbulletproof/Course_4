import requests
from datetime import datetime
import json
import os
from abc import ABC, abstractmethod


class APIManager(ABC):

    @abstractmethod
    def get_vacancies(self):
        """получает вакансии по апи, возвращает список согластно
        запросу пользователя"""
        pass


class Vacancy:
    def __init__(self, name, page, top_n):
        self.name = name
        self.page = page
        self.top_n = top_n

    def __repr__(self):
        return f"{self.name}"


class HeadHunter(Vacancy, APIManager, ABC):
    def __init__(self, name, page, top_n):
        super().__init__(name, page, top_n)
        self.url = 'https://api.hh.ru'

    def get_vacancies(self):
        """Выгрузка данных по 'HH' по запросам пользователя и
        возвращается словарь"""
        data = requests.get(f"{self.url}/vacansies",
                            params={'text': self.name,
                                    'page': self.page,
                                    'per_page': self.top_n}).json()
        return data

    def load_vacancy(self):
        """Проходим циклом по словарю берем из словаря только нужные
        нам данные и записываем их в переменную 'vacancies' """
        data = self.get_vacancies()
        vacancies = []
        for vacancy in data.get('items', []):
            published_at = datetime.strftime(vacancy['published_at'],
                                             "%Y-%m-%dT%H:%M:%S%z")
            vacancy_info = {
                "id": vacancy['id'],
                "name": vacancy['name'],
                "solary_ot": vacancy['salary']['from']
                if vacancy.get('salary') else None,
                "solary_do": vacancy['salary']['to']
                if vacancy.get('salary') else None,
                "responsibility": vacancy['snippet']
                ['responsibility'],
                "data": published_at.strftime("%d.%m.%Y")
            }
            vacancies.append(vacancy_info)

        return vacancies

def job_vacancy():
    """Основной код проекта, после внесения пользователем данных,
    данные сортируются согласно запросу пользователя и вносятся
    в json файл"""

    name = input('Введите вакансию: ')
    top_n = input('Введите кол-во вакансий: ')
    page = int(input('Введите страницу: '))
    hh_instance = HeadHunter(name, page, top_n)
    combined_dict = {'HH': hh_instance.load_vacancy()}

    with open('Found_Vacancies.json', 'w', encoding='utf-8') as file:
        json.dump(combined_dict, file, ensure_ascii=False, indent=2)
