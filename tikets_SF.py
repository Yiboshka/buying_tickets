def tikets_input():
    try:
        tikets = int(input("Выберите количество билетов:"))
        if tikets <= 0:
            print("Количество не может быть равно 0 или отрицательным числом.")
            tikets_input()
        else:
            tikets_input()

    except ValueError:
        print("Введите количество цифрами.")
        tikets_input()

def tikets_all():
    try:
        coast = int()
        total_coast = int()
        for i in range(tikets):
            i += 1
            age = (input(f'Введите возраст посетителя {i}:'))
            age = int(age)
            if age < 18:
                coast = 0
                print("Для несовершеннолетних проход бесплатный.")
            elif 18 <= age <= 25:
                coast = 990
            elif age > 25:
                coast = 1390
        total_coast += coast
        if tikets > 3:
            coast_sale = total_coast - (total_coast * 0.10)
            print("При покупки более 3х билетов действует скидка 10%")
            print("Сумма к оплате с учетом скидки:", coast_sale)
        else:
            print("Сумма к оплате:", total_coast)
    except ValueError:
        print("Введите возраст цифрами.")
        tikets_all()

tikets_input()





