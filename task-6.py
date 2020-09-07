def int_func(text):
    text = list(text)
    text[0] = chr(ord(text[0]) - 32)
    return (''.join(text))


my_list = input("Введите строку, состоящую из слов, разделенных пробелом. \nКаждое слово должно состоять из латинских букв в нижнем регистре: ").split()
for i, j in enumerate(my_list):
    my_list[i] = int_func(j)
print(' '.join(my_list))