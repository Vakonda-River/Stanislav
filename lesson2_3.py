while True:
    ask = int(input("Введите номер месяца в виде целого положительного числа от 1 до 12 :"))
    if ask < 1 or ask > 12:
        print("Вы ошиблись, нет такого месяца. Попробуйте снова.")
        continue
    elif ask >= 1 or ask <= 12:
        break

mes = ["январь","февраль","март","апрель","май","июнь","июль","август","сентябрь","октябрь","ноябрь","декабрь"]
if ask == 12 or ask == 1 or ask == 2:
    print("Это месяц зимы -",mes[ask-1],".")
elif ask == 3 or ask == 4 or ask == 5:
    print("Это месяц весны -",mes[ask-1],".")
elif ask == 6 or ask == 7 or ask == 8:
    print("Это месяц лета -",mes[ask-1],".")
elif ask == 9 or ask == 10 or ask == 11:
    print("Это месяц осени -",mes[ask-1],".")

print("Второй вариант решения.")

mes_d = {1:"январь",2:"февраль",3:"март",4:"апрель",5:"май",6:"июнь",7:"июль",8:"август",9:"сентябрь",10:"октябрь",11:"ноябрь",12:"декабрь"}
if ask == 12 or ask == 1 or ask == 2:
    print("Это месяц зимы -",mes_d[ask],".")
elif ask == 3 or ask == 4 or ask == 5:
    print("Это месяц весны -",mes_d[ask],".")
elif ask == 6 or ask == 7 or ask == 8:
    print("Это месяц лета -",mes_d[ask],".")
elif ask == 9 or ask == 10 or ask == 11:
    print("Это месяц осени -",mes_d[ask],".")

