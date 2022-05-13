import argparse
import typing
from datetime import datetime
from functools import wraps

Dictionary = {'username': 'root', 'password': 'qwerty'}


class UserNotExist(Exception):
    ...


def time_check(login_cd):
    last_login = datetime.now()
    return login_cd - ((datetime.now() - last_login).seconds // 60)


def check_passwd(func):
    @wraps(func)
    def wrapper(username, password):
        if Dictionary.get('login') != username:
            raise UserNotExist("Неправильный логин")
        elif Dictionary.get('password') != password:
            raise UserNotExist("Неправильный пароль")
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


if __name__ == '__main__':
    number_of_attempts = 3
    block_time = 5
    args = parser_input()
    username, password = args.username, args.password

    while number_of_attempts > 0:
        if time_check(block_time) > 0:
            print(f"Вы заблокированы. Следующая попытка через "
                  f"{time_check(block_time)} минут")
            break
        try:
            if login(username, password) and number_of_attempts:
                print("Вы в системе")
                break
        except UserNotExist as logging_error:
            print(logging_error)
            number_of_attempts -= 1
            username = input("Логин: ")
            password = input("Пароль: ")
            if Dictionary.get('login') == username \
                    and Dictionary.get('password') == password:
                print("Вы в системе!")
                break
            else:
                print(f"У вас осталось {number_of_attempts} попыток"
                      if number_of_attempts != 0 else "Попытки истекли!")
