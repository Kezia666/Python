def fact(n):
    for el in range(1, n + 1):
        fact = 1
        i = el
        my_list = []
        while i > 0:
            fact *= i
            if el != i:
                my_list.insert(0, '*')
            my_list.insert(0, str(i))
            i -= 1
        yield f"{el}! = {' '.join(my_list)} = {fact}"


try:
    for el in fact(10):
        print(el)
except (TypeError, NameError):
    print("Incorrect parameter for fact function! You need to enter positive int number!")
