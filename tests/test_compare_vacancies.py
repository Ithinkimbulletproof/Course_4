def test_generate_salary_dict_valid(fixture_class_valid):
    vacancy = fixture_class_valid

    assert isinstance(fixture_class_valid.generate_salary_dict(vacancy.salary_all), dict)
    assert len(fixture_class_valid.generate_salary_dict(vacancy.salary_all)) == 0


def test_generate_salary_dict_some_choice(fixture_class_some_str, fixture_class_number):
    fixture_class_some_str.generate_salary_dict(
        [{"salary": None}, {"salary": {"from": None}}, {"salary": {"from": 100}}])
    assert fixture_class_some_str.salary_all == {'from_None': [{"salary": None}, {"salary": {"from": None}}],
                                                 100: [{"salary": {"from": 100}}]}


def test_get_vacancies_check_salary(fixture_class_valid):
    # Search vacancies wit key "from_None"
    vacancy1 = fixture_class_valid
    salary_none = "from_None"
    salary = 100
    vacancy1.generate_salary_dict([{"salary": None}, {"salary": {"from": None}}, {"salary": {"from": 100}}])
    vacancy1.get_vacancies(vacancy1.salary_all, salary)

    assert vacancy1.salary_all == [{"salary": {"from": 100}}]

    vacancy1.generate_salary_dict([{"salary": None}, {"salary": {"from": None}}, {"salary": {"from": 100}}])
    vacancy1.get_vacancies(vacancy1.salary_all, salary_none)
    assert vacancy1.salary_all == [{"salary": None}, {"salary": {"from": None}}]


def test_get_vacancies_len_is_zero(fixture_class_number):
    vacancy = fixture_class_number
    assert len(vacancy.salary_all) < 2
    assert vacancy.message == "Vacancy not found"


def test_get_top_vacancies_valid(fixture_class_valid):
    vacancy = fixture_class_valid
    vacancy.salary_all = [{"salary": None}, {"salary": {"from": None}}, {"salary": {"from": 100}}]

    assert vacancy.get_top_vacancies() == 'Vacancy not found'

    vacancy = fixture_class_valid
    vacancy.salary_all = [{"salary": None}, {"salary": {"from": None, "to": 1000}},
                          {"salary": {"from": 100, "to": 3000}}]

    assert vacancy.get_top_vacancies() == {3000: [{"salary": {"from": 100, "to": 3000}}],
                                           1000: [{"salary": {"from": None, "to": 1000}}]}


def test_get_vacancies_len_dict(fixture_class_valid):
    vacancy = fixture_class_valid
    assert vacancy.get_vacancies({}, 10000) == "Vacancy not found"
