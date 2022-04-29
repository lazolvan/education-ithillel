h = int(input('Высота: '))
for i in range(h):
    print(' ' * (h - i) + '*' * (i + 1) + '*' * i)