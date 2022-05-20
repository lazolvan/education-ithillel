import argparse
import datetime
import json
import requests
import typing
from datetime import datetime as dt
from dateutil import parser
from functools import wraps


class UserDoesNotExist(Exception):
    ...


def read_data(file_name: str):
    with open(file_name, 'r') as f:
        return json.load(f)


def write_data(file_name: str, data: (dict, list)):
    with open(file_name, 'w') as f:
        return json.dump(data, f, indent=3, ensure_ascii=False)


def user_reg(username: str, password: str):
    data = read_data('login.json')
    date = dt.now()

    registration_data = {username: {
        "password": password,
        "last_login_date": str(date.strftime("%d-%m-%Y, %H:%M:%S"))
    }}
    data.append(registration_data)
    return write_data('login.json', data=data)


def failed_log(username: str):
    failed_log_att = {
        "failed_login_attempt": str(
            dt.now().strftime("%d-%m-%Y, %H:%M:%S"))}
    for user in data:
        try:
            for k in user.keys():
                if k == username:
                    data.append(user.get(username).update(failed_log_att))
                    write_data("failed_login_attempt.json", data=user)
        except AttributeError:
            pass


def check_time(time_cooldown: int) -> int:
    time_now = str(dt.now().strftime("%d-%m-%Y, %H:%M:%S"))
    data = read_data("failed_auth_users.json")
    for v in data.values():
        failed_time_value = v.get("failed_login_attempt")
        return time_cooldown - ((parser.parse(time_now) -
                                 parser.parse(failed_time_value)).seconds // 60)


def check_user_existed(username: str) -> bool:
    for u in data:
        for key in u.keys():
            if username == key:
                return True


def check_passwd(func):
    @wraps(func)
    def wrapper(username: str, passwd: str) -> bool:
        for d in data:
            try:
                if d.get(username).get("password") != passwd:
                    raise UserDoesNotExist ("Неправильное имя или пароль")
            except AttributeError:
                pass
            else:
                return d.get(username).get("password") == passwd

    return wrapper


def parser_input():
    parser = argparse.ArgumentParser(description="Скрипт логина")
    parser.add_argument('-u', dest='username', type=str,
                        help='Логин юзера')
    parser.add_argument('-p', dest='password', type=str,
                        help='Пароль юзера')
    return parser.parse_args()


@check_passwd
def login(username: str, passwd: str) -> bool:
    ...


def authenticate_user(username: str, password: str):
    if login(username, password) and number_of_attempts \
            and check_time(block_time) <= 0:
        return True


def auth_failed_log():
    if check_time(block_time) > 0:
        for key in failed_auth_data.keys():
            if key == username:
                return True


if __name__== '__main__':
    data = read_data("login.json")
    failed_auth_data = read_data("failed_auth_users.json")
    number_of_attempts = 3
    block_time = 5
    args = parser_input()
    username, password = args.username, args.password

    try:
        if login(username if username else input("Введите имя: "), password if
                 password else input("Введите пароль: ")):
            print("Вы вошли!")
    except UserDoesNotExist as err:
        print(err)
    else:
        welcome = input("Зарегистрировать нового юзера [y/n]?: ").lower()
        if welcome == 'y':
            username = str(input("Введите имя: "))
            password = str(input("Введите пароль: "))
            if check_user_existed(username):
                print("Такой юзер уже есть!")
            else:
                user_reg(username, password)
                print("Вы зарегистрированы!")
        elif welcome == 'n':
            print("Хотите войти в систему?")
            username = str(input("Введите имя: "))
            password = str(input("Введите пароль: "))
            while number_of_attempts > 0:
                try:
                    if authenticate_user(username, password):
                        print("Вы вошли!")
                        break
                    elif auth_failed_log():
                        print(f"Вы заблокированы! Следующая попытка через "
                              f"{check_time(block_time)} мин.")
                        break
                    else:
                        if login(username, password):
                            print("Вы вошли!")
                            break
                except UserDoesNotExist as e:
                    print(e)
                    number_of_attempts -= 1
                    failed_log(username)
                    username = input("Имя: ")
                    password = input("Пароль: ")
                    for d in data:
                        try:
                            d.get(username).get("password") == password
                        except AttributeError:
                            pass
                        else:
                            if number_of_attempts != 0:
                                print(f"Осталось {number_of_attempts} попыток")
                            else:
                                print(f"Вы заблокированы! \n Следующая попытка через "
                                      f"{check_time(block_time)} мин.")
                                break

