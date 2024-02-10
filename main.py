from UserInteraction import UserInteraction


def main():
    user_input = input("Please, write name\nof vacancy for search: ")

    while True:
        users_salary = input("Text salary if you want\n"
                             "to see vacancies with salary:\n")
        if users_salary.isdigit():
            break
        print("\nPlease, text number or 'Enter...\n")

    user = UserInteraction(user_input)

    while True:
        users_city = input("Now, you need text your city:\n").capitalize()
        if users_city.isalpha():
            break
        print("\nI don't know about this city.\n")

    user.sorted_salary(user.all_vacancy, int(users_salary), users_city)
    user.get_top_vacancies(user.sort_salary)

    user.make_info(user.top_salary)

    while True:
        number_vacancy = input("Choose number of top vacancy\n"
                               "if you want to see more: ")
        if number_vacancy.isdigit():
            break

    print(user.last_info(user.vacancies_list, number_vacancy))


if __name__ == '__main__':
    main()
