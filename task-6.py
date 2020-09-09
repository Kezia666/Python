from itertools import count, cycle

my_list = []

for i in count(3):
    if i == 10:
        break
    else:
        my_list.append(i)

iter = cycle(my_list)

print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
