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
        data = requests.get()