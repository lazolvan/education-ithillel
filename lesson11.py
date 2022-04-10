import random
import string

dict1 = {k: v for k, v in
         zip([random.choice(string.ascii_lowercase) for _ in range(10)],
             [random.randint(1, 100) for _ in range(10)])}
dict2 = {k: v for k, v in
         zip([random.choice(string.ascii_lowercase) for _ in range(10)],
             [random.randint(1, 100) for _ in range(10)])}
dict3 = dict1 | dict2

print(dict1)
print(dict2)
for k, v in dict3.items():
    if k in dict1.keys():
        v = dict1[k] if v < dict3[k] else v
    dict3[k] = v
print(dict3)
