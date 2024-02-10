import pytest
from CompareVacancies import CompareVacancies


@pytest.fixture
def fixture_class_valid():
    return CompareVacancies('python')


@pytest.fixture
def fixture_class_number():
    return CompareVacancies(1)


@pytest.fixture
def fixture_class_some_str():
    return CompareVacancies('666999')
