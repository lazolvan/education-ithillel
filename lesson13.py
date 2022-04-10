def square(x):
    return x * 4, x ** 2, (2 * x ** 2) ** .5


result = square(int(input("Введите сторону квадрата: ")))
print(result)
