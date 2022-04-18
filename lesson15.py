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


if __name__ == '__main__':
    number_of_attempts = 3
    while number_of_attempts > 0:
        login_input = str(input("Введите логин: "))
        passwd_input = str(input("Введите пароль: "))
        if login(login_input, passwd_input):
            print("Вы в системе!")
            break
        number_of_attempts -= 1
        print("Не правильный Логин или Пароль")
        print(f"У вас осталось {number_of_attempts} попыток" if number_of_attempts != 0
              else "Попытки истекли!")
