import random
numbers = [random.randint(1, 10) for _ in range(10)]
numbers2 = [random.randint(1, 10) for _ in range(10)]
unique = [i for i in (numbers + numbers2) if (numbers + numbers2).count(i) == 1]
print({len(unique)})
