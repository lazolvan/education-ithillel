def multiply(x):
    result = 1
    for i in x:
        if int(i) != 0:
            result *= int(i)
    return result


x = input()
print("Произведение цифр:", multiply(x))