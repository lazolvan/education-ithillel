a = input('Введите что-то: ')
b = 'Это строка в которую {} новую строку'.format(a)

print(b)

b = b.replace(a, 'замена в строке')
print(b)

print(len(b))

if b.find('строка') != -1:
    print('да')
else:
    print('no')


