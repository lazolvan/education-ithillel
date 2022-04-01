import random
a = [x for x in random.sample(range(150, 200), 10)]
height_input = int(input("Введите рост Петра: "))
a.append(height_input)
a.sort(reverse=True)
print(a)
for i in range(len(a)):
    if a[i] == height_input:
        print(a.index(height_input) + a.count(height_input))
