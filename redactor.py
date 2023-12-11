import hashlib
import os

def init_file():  # Инициализация файла, если этого не сделать програма вылетит м ошибкой, что файла нет
    """Создает файл пользователей"""
    if not os.path.exists('users.txt'):
        with open('users.txt', 'w'):
            pass


def add_user(login: str, password: str) -> bool:
    """Добавляет пользователя в файл"""
    with open('users.txt', 'r') as f:
        users = f.read().splitlines()  # Считываем всех пользователей из файла

    for user in users:
        args = user.split(':')
        if login == args[0]:  # Если логин уже есть, парль не проверяем, шанс взлома увеличится(кто-то мб узнает пароль)
            return False  # Тут можно написать что угодно, будь то HTML статус(409 - conflict), либо просто фразу ошибки

    with open('users.txt', 'a') as f:
        f.write(f'{login}:{password}\n')  # Добавляем нового пользователя
    return True


def get_user(login: str, password: str) -> bool:
    """Проверяет логин и пароль пользователя"""
    with open('users.txt', 'r') as f:
        users = f.read().splitlines()  # Считываем всех пользователей из файла

    for user in users:
        args = user.split(':')
        if login == args[0] and password == args[1]:  # Если пользователь с таким логином и паролем существует
            return True
    return False


def main_loop(login: str):
    """Главный цикл программы"""
    print(f'Привет, {login}!')  # Тут основная часть программы


init_file()

while True:
    print('''Добро пожаловать! Выберите пункт меню:
    1. Вход
    2. Регистрация
    3. Выход''')

    user_input = input()
    if user_input == '1':  # Условия можно заменить на: user_input.lower() == 'вход'
        print('Введите логин:')
        login = input()

        print('Введите пароль:')
        password = input()

        result = get_user(login, hashlib.sha256(password.encode()).hexdigest())

        if result:
            print('Вы вошли в систему')
            break  # Выходим из цикла
        else:
            print('Неверный логин или пароль')

    elif user_input == '2':
        print('Введите логин:')
        login = input()

        print('Введите пароль:')
        password = input()

        print('Повторите пароль:')
        password_repeat = input()

        if password != password_repeat:
            print('Пароли не совпадают!')
            continue

        result = add_user(login, hashlib.sha256(
            password.encode()).hexdigest())  # Вызываем функцию добавления пользователя. И хешируем пароль(безопасность)

        if not result:
            print('Пользователь с таким логином уже существует')
        else:
            print('Регистрация прошла успешно!')

    elif user_input == '3':
        print('Завершение работы')
        break  # Выходим из цикла

    import os

# Задаем путь к директории, где хранятся файлы
directory = 'C:\Users\as5\Desktop\rabota'
# Проверяем, существует ли директория
if not os.path.exists(directory):
    # Если директория не существует, выдаем ошибку
    raise FileNotFoundError('Директория не найдена')
else:
    # Иначе перебираем все файлы в директории
    for redactor in os.listdir(directory):
        # Если файл является директорией, пропускаем его
        if os.path.isdir(os.path.join(directory, redactor)):
            continue
        else:
            # Иначе открываем файл и выполняем с ним некоторые действия
            with open(os.path.join(directory, redactor), 'r') as file:
                # Читаем содержимое файла
                contents = file.read()
                # Здесь выполняем некоторые действия с содержимым файла
                print(f'Файл: {redactor}')
# Закрываем файл
file.close()

choice = int(input("Введите число от 1 до 3: "))
if choice == 1:
    print("Вы выбрали действие 1.")
elif choice == 2:
    print("Вы выбрали действие 2.")
elif choice == 3:
    print("Вы выбрали действие 3.")
else:
    print("Пожалуйста, введите число от 1 до 3.")
