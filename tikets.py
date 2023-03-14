tikets = input("Выберите количество билетов:")
tikets = int(tikets)

def tikets_all():
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

tikets_all()





