from abc import ABC
import pytest

from config import DATA
from GetVacancies import GetVacancies
from AbstractHh import AbstractHh


def test_issubclass():
    assert issubclass(AbstractHh, ABC)
    assert issubclass(GetVacancies, AbstractHh)


def test_get_vacancy_from_api():
    vacancy1 = GetVacancies('tttttt')
    vacancy2 = GetVacancies(1)
    vacancy3 = GetVacancies('python')

    vacancy1.get_vacancy_from_api()
    vacancy2.get_vacancy_from_api()
    vacancy3.get_vacancy_from_api()

    assert vacancy1.message == "Vacancies found"
    assert vacancy2.message == "Vacancy not found"
    assert vacancy3.message == "Vacancies found"


def test_save_info_valid():
    vacancy1 = GetVacancies('python')

    assert isinstance(vacancy1.all, list)
    assert len(vacancy1.all) > 0


def test_save_info_zero_len():
    vacancy1 = GetVacancies(1)

    vacancy1.save_info()
    assert vacancy1.message == "Vacancy not found"
