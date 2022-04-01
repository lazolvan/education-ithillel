text = input('Введите текст:')
result = {}
for i in text.split():
    if not result.get(i) == None:
        result[i] += 1
    else:
        result[i] = 1
for i, a in result.items():
    print(f'Слово: {i}, Количество: {a}')
