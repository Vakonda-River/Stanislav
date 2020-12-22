text = "Ваша компания получила"
text2 = "В пересчёте на одного сотрудника прибыль составляет "
val = " ( y.e.)."
info = " прибыль, которая составила "
info2 = " убыток. "
ask1 = "Введите сумму выручки Вашей компании за указанный период : "
ask2 = "Введите сумму затрат/издержек Вашей компании за указанный период : "
ask3 = "Введите количество сотрудников в штате компании : "
f = " %."

proc = float(input(ask1))
cost = float(input(ask2))
res = proc - cost
rent = round(((proc / cost) * 100 - 100), 2)
if res > 0 :
    print(text , info , rent , f)
    pers = int(input(ask3))
    print (text2 , round((res / pers) , 2) , val)
else:
    print(text , info2)
