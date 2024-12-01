age = int(input("Ваш возраст: "))
citizen = input("Вы являетесь гражданином страны? (да/нет): ")
discvalification = input("Вы отбываете уголовное наказание? (да/нет): ")


if age >= 18 and citizen == 'да' and not discvalification == 'да':
    print("Вы можете участвовать в выборах")
else:
    print("Вы не можете участвовать в выборах")