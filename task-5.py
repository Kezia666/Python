res = 0
flag = True


def my_func(list_param):
    global res, flag
    for i in list_param:
        try:
            res += float(i)
        except ValueError:
            if i == "*":
                flag = False
                break
    return (res)


while flag:
    my_list = list(input("Введите строку чисел, разделенных пробелами. Если хотите завершуть работу программы - введите символ '*': ").split())
    print(f"Сумма: {my_func(my_list)}")
