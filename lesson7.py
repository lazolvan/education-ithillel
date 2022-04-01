import random
list1 = [random.randint(1, 10) for _ in range(10)]
count = 0
for i in range(1, (len(list1)) -1):
    if list1[i] > list1[i -1] + list1[i +1]:
        count += 1
print(list1, {count})
