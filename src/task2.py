import faker
import os
# У вас є текстовий файл, який містить інформацію про котів. Кожен рядок файлу містить унікальний ідентифікатор кота, його ім'я та вік, розділені комою. Наприклад:

# 60b90c1c13067a15887e1ae1,Tayson,3
# 60b90c2413067a15887e1ae2,Vika,1
# 60b90c2e13067a15887e1ae3,Barsik,2
# 60b90c3b13067a15887e1ae4,Simon,12
# 60b90c4613067a15887e1ae5,Tessi,5

# Ваше завдання - розробити функцію get_cats_info(path), яка читає цей файл та повертає список словників з інформацією про кожного кота.

# КОТОГЕНЕРАТОР


class Cat:
    def __init__(self, cat_data):
        self.nick = cat_data.first_name()
        self.chip = cat_data.bothify(text='##'+'?'+'##'+'?' +
                                     '#######'+'?'+'#####'+'?'+'#'+'??'+'#')
        self.age = cat_data.random_int(1, 25)

    def generate_cat(self):
        return f'{self.chip},{self.nick},{self.age}'


cat_data = faker.Faker()


def write_to_file_cats(path: str, number_of_cats: int):
    with open(path, 'w+') as file:
        for _ in range(number_of_cats):
            data = Cat(cat_data).generate_cat()
            file.write(data + '\n')


# write_to_file_cats('task2.txt', 13)
# КОТОГЕНЕРАТОР КІНЕЦЬ


# Завдання 2
def read_from_file_cats(path: str):
    cats = []
    if not os.path.exists(path):
        raise FileNotFoundError(f"Файл '{path}' не існує.")
    with open(path, 'r', encoding='utf-8') as file:

        for line in file:
            if not line:
                raise ValueError("Файл пустий.")
            cat_dict = {}
            line = line.strip().split(',')
            cat_dict = {'chip': line[0], 'nick': line[1], 'age': line[2]}
            cats.append(cat_dict)
    return cats


print(read_from_file_cats('task2.txt'))
