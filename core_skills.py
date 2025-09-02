import random

rand_list = []

for i in range(10):
    rand_list.append(random.randint(0,20))

print(rand_list)

list_comprehension_below_10 = []
for i in rand_list:
    if i < 10:
        list_comprehension_below_10.append(i)
print(list_comprehension_below_10)


def lower_ten(n):
    return n < 10

list_comprehension_below_10_filter = filter(lower_ten, rand_list)
print(list(list_comprehension_below_10_filter))
