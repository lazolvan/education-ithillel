import argparse
from datetime import datetime
from functools import wraps


def check_passwd(func):
    @wraps(func)
    def wrapper(username, password):
        return Dictionary.get('login') == username \
                and Dictionary.get('password') == password
    return wrapper


def authenticate(passwd):
    ...


def parser_input():
    parser = argparse.ArgumentParser(description="Login enter")
    parser.add_argument('-u', dest='username', type=str,
                        help='user login credentials')
    parser.add_argument('-p', dest='password', type=str,
                        help='user pass credentials')
    return parser.parse_args()


@check_passwd
def login(username: str, password: str) -> bool:
    ...


def time_check(login_cd):
    last_login = datetime.now()
    return login_cd - ((datetime.now() - last_login). seconds // 60)


if __name__ == '__main__':
    Dictionary = {'login': 'root', 'password': 'qwerty'}
    number_of_attempts = 3
    block_time = 5
    args = parser_input()
    username, password = args.username, args.password

    while number_of_attempts > 0:
        if time_check(block_time) > 0:
            print(f"Вы заблокированы. Следующая попытка через "
                  f"{time_check(block_time)} минут")
            break
        if login(username=username, password=password) and number_of_attempts:
            print("Вы в системе")
            break
        else:
            number_of_attempts -= 1
            print("Не правильный Логин или Пароль")
            print(f"У вас осталось {number_of_attempts} попыток"
                if number_of_attempts != 0 else "Попытки истекли!")
