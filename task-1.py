greeting = "Добро пожаловать на наш сайт!"
user_count = 57834

print(greeting)
print(f"За сегодня вы наш {user_count}-й посетитель!")

name = input("Введите ваше имя: ")
surname = input("Введите вашу фамилию: ")
age = int(input("Введите ваш возраст: "))
phone = int(input("Введите ваш номер телефона (только цифры 0-9): "))

print(f"Вас зовут {name} {surname}. Вам {age} лет. Мы обязательно перезвоним вам по номеру {phone}. Всего доброго!")