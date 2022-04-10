def square(x):
    return x * 4, x ** 2, 2 ** 0.5 * x


result = square(int(input("Введите сторону квадрата: ")))
print(result)
