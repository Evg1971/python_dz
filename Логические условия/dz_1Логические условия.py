age = int(input("Ваш возраст: "))
citizen = input("Вы являетесь гражданином страны? (да/нет): ").strip().lower()
discvalification = input("Вы отбываете уголовное наказание? (да/нет): ").strip().lower()


if age >= 18 and citizen == 'да' and not discvalification == 'да':
    print("Вы можете участвовать в выборах")
else:
    print("Вы не можете участвовать в выборах")