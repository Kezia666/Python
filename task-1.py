my_list = [1, 3.14, 5-6j, True, "Hi", b"Test", bytearray(b"text"), [1, 2], {1: 15, 8: 3}, (1, 2, 3), None, set([1, 2])]

# Variant 1
for i in my_list:
    print(type(i))

# Variant 2
for i, j in enumerate(my_list):
    print(type(my_list[i]))