from datetime import datetime
from functools import wraps

Dictionary = {'login': 'root', 'password': 'qwerty'}


def check_passwd(func):
    @wraps(func)
    def wrapper(username, passwd):
        return Dictionary.get('login') == username \
                and Dictionary.get('password') == passwd
    return wrapper


def authenticate(passwd):
    ...


@check_passwd
def login(username: str, passwd: str) -> bool:
    ...


def time_check(login_cd):
    last_login = datetime.now()
    return login_cd - ((datetime.now() - last_login). seconds // 60)


if __name__ == '__main__':
    number_of_attempts = 3
    block_time = 5
    while number_of_attempts > 0:
        if time_check(block_time) > 0:
            print(f"Вы заблокированы. Следующая попытка через "
                  f"{time_check(block_time)} минут")
            break
        else:
            login_input = str(input("Введите логин: "))
            passwd_input = str(input("Введите пароль: "))
            if login(login_input, passwd_input):
                print("Вы в системе!")
                break
        number_of_attempts -= 1
        print("Не правильный Логин или Пароль")
        print(f"У вас осталось {number_of_attempts} попыток" if number_of_attempts != 0
              else "Попытки истекли!")
