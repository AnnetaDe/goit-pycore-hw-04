# У вас є текстовий файл, який містить інформацію про місячні заробітні плати розробників у вашій компанії. Кожен рядок у файлі містить прізвище розробника та його заробітну плату, які розділені комою без пробілів.

# Наприклад:

# Alex Korp, 3000
# Nikita Borisenko, 2000
# Sitarama Raju, 1000

# Ваше завдання - розробити функцію total_salary(path), яка аналізує цей файл і повертає загальну та середню суму заробітної плати всіх розробників.
import faker

fake_person = faker.Faker()
fake_salary = faker.Faker()


def fake_data(lines: int):
    with open('task1.txt', 'w+') as file:
        for _ in range(lines):
            salary = fake_salary.random_int(1000, 10000)
            person = fake_person.name()
            file.writelines(f'{person}, {salary}\n')


# fake_data(lines=13)

def total_salary(path: str):
    with open(path, 'r', encoding='utf-8') as file:
        data = file.readlines()
        for line in data:
            total_salary = sum(int(line.split(', ')[1]) for line in data)
            average_salary = total_salary / len(data)
    return total_salary, average_salary.__round__(2)


print(total_salary('task1.txt'))
