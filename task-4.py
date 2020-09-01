string = input("Введите строку из нескольких слов, разделённых пробелами: ")

my_list = string.split()
for i, j in enumerate(my_list):
    print(i+1, j[0:10])